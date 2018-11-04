const path = require('path');

const config = {
    entry: {
        main: path.join(__dirname, 'src', 'marlin', 'js', 'index.js'),
        style: path.join(__dirname, 'src', 'marlin', 'css', 'index.scss'),
    },
    output: {
        publicPath: '/assets/',
    },
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
            Util: path.join(__dirname, 'src', 'marlin', 'js', 'util.js'),
            Actions: path.join(__dirname, 'src', 'marlin', 'js', 'actions'),
            Components: path.join(__dirname, 'src', 'marlin', 'js', 'components'),
        }
    },
};

if (process.env.FLASK_ENV === 'development') {
    config.mode = 'development';
}
else {
    config.mode = 'production';
}

module.exports = config;
