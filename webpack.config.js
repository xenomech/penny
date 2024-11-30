const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const outputStaticDir = path.resolve(__dirname, "core/static");
const entryScript = path.resolve(__dirname, "frontend/scripts/index.ts");
const mode = process.env.NODE_ENV || "development";

module.exports = {
  mode: mode,
  entry: entryScript,
  output: {
    filename: "js/[name]-[contenthash].js",
    path: outputStaticDir,
    clean: true,
    publicPath: "auto",
  },
  resolve: {
    extensions: [".ts", "..."],
  },
  plugins: [
    new BundleTracker({
      path: outputStaticDir,
      filename: "webpack-stats.json",
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name]-[contenthash].css",
    }),
  ],
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        include: path.resolve(__dirname, "frontend/scss"),
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "sass-loader",
            options: {
              implementation: require("sass"),
            },
          },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  "postcss-preset-env",
                  require("tailwindcss")("./tailwind.config.js"),
                  require("autoprefixer"),
                ],
              },
            },
          },
        ],
      },
      {
        test: /\.ts$/,
        use: ["ts-loader"],
        exclude: /node_modules/,
      },
    ],
  },
};
