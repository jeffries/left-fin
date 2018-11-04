const path = require('path');

const config = {
    entry: {
        main: path.join(__dirname, 'src', 'marlin', 'index.js'),
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
                    { loader: 'style-loader' },
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
            },
        ],
    },
    resolve: {
        extensions: [
            '.js',
            '.jsx',
            '.scss',
        ],
        mainFiles: [
            'index.js',
            'Index.jsx',
        ],
        alias: {
            Actions: path.join(__dirname, 'src', 'marlin', 'actions'),
            Components: path.join(__dirname, 'src', 'marlin', 'components'),
        },
    },
};

if (process.env.FLASK_ENV === 'development') {
    config.mode = 'development';
}
else {
    config.mode = 'production';
}

module.exports = config;
