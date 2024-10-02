import requests
import os

from github import Github

# Token 준비
PRIVATE_ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
SLACK_TOKEN = os.environ['SLACK_TOKEN']

g = Github(PRIVATE_ACCESS_TOKEN)
repo = g.get_repo("altsoft5472344/ondaji_4gen_front_rn")

labels = repo.get_labels()


# Slack 메세지 전송 함수
# [설정] channel 명을 설정 #채널명
def _send_slack(msg: str):
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + SLACK_TOKEN},
        data={"channel": "#pull_request", "text": msg},
    )

# 라벨 하루씩 줄이기
def _set_label_decrease(pull, before_labels) -> str:
    new_label = None
    if "D-3" in before_labels:
        new_label = "D-2"
    elif "D-2" in before_labels:
        new_label = "D-1"
    elif "D-1" in before_labels:
        new_label = "D-0"
    
    if new_label:
        # 기존 라벨에 새로운 라벨 추가
        pull_labels = [label.name for label in pull.get_labels()]
        filtered_labels = [label for label in pull_labels if not label.startswith('D-')]
        filtered_labels.append(new_label)
        pull.set_labels(*filtered_labels)
        return filtered_labels
    
    return before_labels
    


# PR 링크 생성 함수
# [설정] link 설정 - https://github.com/organization-name/repo-name/pull/
def _make_pr_link_with_no(pr_no: int) -> str:
    link = f"https://github.com/altsoft5472344/ondaji_4gen_front_rn/pull/" + str(pr_no)
    return link


# PR 목록 조회 함수
def _get_total_pull_requests():
    count = 0
    pull_requests_list = []
    # 현재 열려있는 PR 목록들을 가져온다.
    for pull in repo.get_pulls(
        state="open",
        sort="updated",
    ):
        count += 1
        pull_requests_list.append(pull)
    return count, pull_requests_list


# Slack 메세지 생성, 전송 함수
# PR 올라온 개수와 어는 PR이 있는 지 메세지에 작성된다.
# 본 메세지에는 리뷰자의 이름도 들어가서 해당 PR에 대한 리뷰가 누가 맡았는 지 확인할 수 있다.
def set_pull_requests_tags():
    cnt, pulls = _get_total_pull_requests()
    pr_msg_to_slack = (
        f"[FrontEnd_RN]👋🏻 총 {cnt}개의 Pull Request가 리뷰를 기다리고 있어요!\n"
    )

    for pull in pulls:

        pr_link = _make_pr_link_with_no(pull.number)

        if pull.labels == []:
            # D-1 라벨 설정
            pull.set_labels("D-1")
            pr_msg_to_slack += f"> <{pr_link}|[ D-1 ] " + pull.title + ">" + "\n"
        elif pull.get_labels()[0].name == "D-0":
            # D-0 라벨인 경우
            pr_msg_to_slack += f"> <{pr_link}|[ D-0 ] " + pull.title + ">" + "\n"
        else:
            # D-0 라벨이 아닌 라벨이 있다면, 하루를 줄인 태그를 설정한다.
            labels = pull.get_labels()
            label_names = [label.name for label in labels] 
            after_labels = _set_label_decrease(pull, label_names)
            # D-로 시작하는 데이터와 나머지 데이터를 분리
            d_labels = [label for label in after_labels if label.startswith('D-')]
            other_labels = [label for label in after_labels if not label.startswith('D-')]
            sorted_labels = d_labels + other_labels
            pr_msg_to_slack += (
                f"> <{pr_link}|[ " + sorted_labels[0] + " ] " + pull.title + ">" + "\n"
            )
    _send_slack(pr_msg_to_slack)


set_pull_requests_tags()
