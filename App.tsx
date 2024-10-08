import React, { useEffect } from 'react';
import { Platform, SafeAreaView, StyleSheet } from 'react-native';
import SplashScreen from 'react-native-splash-screen';
import WebView from 'react-native-webview';

const SPLASH_SCREEN_DELAY = 2000;

const styles = StyleSheet.create({
  safearea: { flex: 1, backgroundColor: '#fff' },
});

export default function App() {
  useEffect(() => {
    setTimeout(() => {
      SplashScreen.hide();
    }, SPLASH_SCREEN_DELAY);
  });

  return (
    <SafeAreaView style={styles.safearea}>
      <WebView
        source={{
          uri:
            Platform.OS === 'android'
              ? `http://10.0.2.2:3000/onboarding`
              : `http://localhost:3000/onboarding`,
        }}
        webviewDebuggingEnabled
        scrollEnabled={false}
      />
    </SafeAreaView>
  );
}
