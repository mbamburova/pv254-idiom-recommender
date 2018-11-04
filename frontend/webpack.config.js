/* eslint-disable object-curly-newline */
/* eslint-disable object-property-newline */
/* eslint-disable no-path-concat */
const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const mode = process.env.NODE_ENV || 'development';

module.exports = {
  entry: './src/index.jsx',
  output: {
    path: path.resolve(__dirname, './build'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: [
          'babel-loader',
          'eslint-loader'
        ]
      },
      {
        test: /\.(ts|tsx)$/,
        exclude: /node_modules/,
        use: [
          'ts-loader',
          { loader: 'tslint-loader', options: { configFile: 'tslint.json' } }
        ]
      },
      {
        test: /\.css$/,
        include: [
          path.resolve(__dirname, './node_modules')
        ],
        use: [
          { loader: 'file-loader', options: { name: 'styles/[name].[ext]' } },
          { loader: 'extract-loader', options: { publicPath: '../' } },
          { loader: 'css-loader' }
        ],
      },
      { test: /\.css$/,
        exclude: [
          path.resolve(__dirname, './node_modules')
        ],
        use: [
          { loader: "style-loader" },
          { loader: "css-loader" }
        ]
      },
      { test: /\.less$/,
        exclude: [
          path.resolve(__dirname, './node_modules')
        ],
        use: [
          { loader: "style-loader" },
          { loader: "css-loader" },
          { loader: "less-loader" }
        ]
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2)/,
        use: [
          { loader: 'url-loader', options: { name: 'assets/[name].[ext]', limit: 10000 } }
        ]
      },
      {
        test: /\.(html|jpg|jpeg|png|ico|gif)/,
        use: [
          { loader: 'file-loader', options: { name: '[path][name].[ext]', context: 'public' } }
        ]
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx']
  },
  plugins: [
    new CleanWebpackPlugin(['build'])
  ],
  devtool: mode === 'development' ? 'eval-source-map' : null,
  devServer: {
    contentBase: path.resolve(__dirname, './build'),
    port: 3000,
    open: true,
  }
};
