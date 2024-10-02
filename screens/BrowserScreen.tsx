import React from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
import WebView from 'react-native-webview';

const styles = StyleSheet.create({
  safearea: { flex: 1 },
});

export default function BrowserScreen() {
  return (
    <SafeAreaView style={styles.safearea}>
      <WebView source={{ uri: 'http://10.0.2.2:3000' }} webviewDebuggingEnabled></WebView>
    </SafeAreaView>
  );
}
