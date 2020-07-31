const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');

const assetDir = './frontend/assets';

module.exports = {
    context: __dirname,
    entry: `${assetDir}/main`,
    output: {
        path: path.resolve(`${assetDir}/dist`),
        filename: "[name]-[hash].js",
    },

    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                exclude: /node_modules/,
                use: [
                    // fallback to style-loader in development
                    // process.env.NODE_ENV !== 'production'
                    //     ? 'style-loader'
                    //     : MiniCssExtractPlugin.loader,
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            },
        ],
    },

    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: `${assetDir}/dist/webpack-stats.json`,
        }),

        new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: '[name].css',
            chunkFilename: '[id].css',
        }),

        new VueLoaderPlugin(),
        new CleanWebpackPlugin(),
    ],

    resolve: {
        alias: {
            vue: "vue/dist/vue.js",
        }
    }, 

    watchOptions: {
        aggregateTimeout: 300,
        poll: 1000,
    }
};