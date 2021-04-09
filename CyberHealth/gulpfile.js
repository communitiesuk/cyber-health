"use strict";
const gulp = require("gulp");
const del = require("del");
const sass = require("gulp-dart-sass");
const postcss = require('gulp-postcss')
const autoprefixer = require('autoprefixer')
const concat = require("gulp-concat");
const path = require("path");

// Root path
const repoRoot = path.join(__dirname);

// Npm paths
const npmRoot = path.join(repoRoot, "node_modules");
const govukFrontendRoot = path.join(npmRoot, "govuk-frontend");
const govukFrontendFontsFolder = path.join(
  govukFrontendRoot,
  "govuk",
  "assets",
  "fonts"
);
const govukFrontendImagesFolder = path.join(
  govukFrontendRoot,
  "govuk",
  "assets",
  "images"
);

// Dist folders
const distFolder = path.join(repoRoot, "static", "dist");
const distCssFolder = path.join(distFolder, "css");
const distFontsFolder = path.join(distFolder, "fonts");
const distImagesFolder = path.join(distFolder, "images");

// Src folders
const srcFolder = path.join(repoRoot, "static", "src");
const srcScssFolder = path.join(srcFolder, "scss");

// Clean tasks
gulp.task("clean:css", function () {
  return del(distFontsFolder + "/**/*").then(function (paths) {
    console.log("💥  Deleted the following CSS files:\n", paths.join("\n"));
  });
});

gulp.task("clean:fonts", function () {
  return del(distCssFolder + "/**/*").then(function (paths) {
    console.log("💥  Deleted the following font files:\n", paths.join("\n"));
  });
});

gulp.task("clean:images", function () {
  return del(distImagesFolder + "/**/*").then(function (paths) {
    console.log("💥  Deleted the following image files:\n", paths.join("\n"));
  });
});

gulp.task("clean", gulp.parallel("clean:css", "clean:fonts", "clean:images"));

// Sass compiling
const sassOptions = {
  outputStyle: "compressed",
  lineNumbers: true,
};


gulp.task("sass", function () {
  return gulp
    .src(srcFolder + "/**/*.scss")
    .pipe(concat("styles.scss"))
    .pipe(sass(sassOptions).on("error", sass.logError))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest(distCssFolder));
});


// Copy assets from GOV UK frontend
function copyFactory(resourceName, sourceFolder, targetFolder) {
  return function () {
    return gulp
      .src(sourceFolder + "/**/*", { base: sourceFolder })
      .pipe(gulp.dest(targetFolder))
      .on("end", function () {
        console.log("📂  Copied " + resourceName);
      });
  };
}

gulp.task(
  "copy:govuk_frontend_assets:fonts",
  copyFactory(
    "fonts from the GOVUK frontend assets",
    govukFrontendFontsFolder,
    distFontsFolder
  )
);

gulp.task(
  "copy:govuk_frontend_assets:images",
  copyFactory(
    "fonts from the GOVUK frontend assets",
    govukFrontendImagesFolder,
    distImagesFolder
  )
);

gulp.task(
  "copyAssets",
  gulp.parallel(
    "copy:govuk_frontend_assets:fonts",
    "copy:govuk_frontend_assets:images"
  )
);

// Compile & build
gulp.task("compile", gulp.parallel("copyAssets", "sass"));
gulp.task("build", gulp.series("clean", "compile"));

// Watch for changes
gulp.task("watch:css", function () {
   gulp.watch([srcScssFolder + "/**/*.scss"], gulp.series("sass"));
 })

gulp.task(
  "watch",
  gulp.series("build", "watch:css")
);


