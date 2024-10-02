module.exports = module.exports = {
  root: true,
  env: {
    es6: true,
    browser: true,
    node: true,
    'react-native/react-native': true,
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: './tsconfig.json',
  },
  extends: [
    'airbnb',
    'airbnb-typescript',
    'airbnb/hooks',
    'plugin:prettier/recommended',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/recommended',
  ],
  plugins: ['@typescript-eslint', 'prettier', 'react', 'react-native'],
  rules: {
    'react/prop-types': 'off',
    'react/jsx-boolean-value': 0,
    'no-unused-vars': 'warn',
    'no-console': 'off',
    'no-param-reassign': 0,
    'react/jsx-props-no-spreading': 'off',
    'react/jsx-no-useless-fragment': 0,
    'import/prefer-default-export': 0,
    'react-hooks/exhaustive-deps': 0,
    'import/no-extraneous-dependencies': 0,
    'react/require-default-props': 0,
    'react/no-unknown-property': 'off',
    'prettier/prettier': [
      'error',
      {
        endOfLine: 'auto',
      },
    ],
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};
