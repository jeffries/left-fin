const path = require('path');

module.exports = {
    entry: {
        main: path.join(__dirname, 'src', 'js', 'index.js'),
        style: path.join(__dirname, 'src', 'css', 'index.scss'),
    },
    output: {
        path: path.join(__dirname, 'build', 'public'),
        publicPath: 'http://localhost:5001/assets/',
        // filename: '[name].[chunkhash].js',
        // chunkFilename: '[id].[chunkhash].js',
    },
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                use: [
                    { loader: 'babel-loader' },
                ],
            },
            {
                test: /\.(scss)$/,
                use: [
                    { loader: 'style-loader'},
                    { loader: 'css-loader' },
                    {
                        loader: 'postcss-loader',
                        options: {
                            plugins: function() {
                                return [
                                    require('precss'),
                                    require('autoprefixer'),
                                ];
                            },
                        },
                    },
                    { loader: 'sass-loader' },
                ],
            }
        ],
    },
    resolve: {
        extensions: [
            '.js',
            '.jsx',
        ],
        mainFiles: [
            'index.js',
            'Index.jsx',
        ],
        alias: {
            Util: path.join(__dirname, 'src', 'js', 'util.js'),
            Actions: path.join(__dirname, 'src', 'js', 'actions'),
            Components: path.join(__dirname, 'src', 'js', 'components'),
        }
    },
}
