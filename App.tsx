import React, { useEffect } from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
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
      <WebView source={{ uri: `https://test.ondaji.com/villages` }} webviewDebuggingEnabled />
    </SafeAreaView>
  );
}
