"use strict";
const gulp = require("gulp");
const del = require("del");
const sass = require("gulp-dart-sass");
const postcss = require('gulp-postcss')
const autoprefixer = require('autoprefixer')
const concat = require("gulp-concat");
const path = require("path");
const debug = require('gulp-debug');
var rename = require("gulp-rename");

// Root path
const repoRoot = path.join(__dirname);

// Npm paths
const npmRoot = path.join(repoRoot, "node_modules");
const govukFrontendRoot = path.join(npmRoot, "govuk-frontend");
const tinyMCERoot = path.join(npmRoot, "tinymce");

const tinyMCELangRoot = path.join(npmRoot, "tinymce-i18n", "langs5");
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

const govukFrontendScriptsFolder = path.join(
  govukFrontendRoot,
  "govuk");

// Dist folders
const distFolder = path.join(repoRoot, "static", "dist");
const distCssFolder = path.join(distFolder, "css");
const distFontsFolder = path.join(distFolder, "fonts");
const distImagesFolder = path.join(distFolder, "images");
const distScriptFolder = path.join(distFolder, "scripts");
const distTinyMCEFolder = path.join(distFolder, "tinymce");
const distTinyMCELangFolder = path.join(distFolder, "tinymce", "langs");

// Src folders
const srcFolder = path.join(repoRoot, "static", "src");
const srcScssFolder = path.join(srcFolder, "scss");
const srcTypographyScssFolder = path.join(srcFolder, "typography_scss");

const srcScripts = path.join(srcFolder, "scripts");

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


gulp.task("clean:script", function () {
  return del(distScriptFolder + "/*").then(function (paths) {
    console.log("💥  Deleted the following script files:\n", paths.join("\n"));
  });
});



gulp.task("clean:tinymce", function () {
  return del(distTinyMCEFolder + "/*").then(function (paths) {
    console.log("💥  Deleted the following tinymce files:\n", paths.join("\n"));
  });
});


gulp.task("clean", gulp.parallel("clean:css", "clean:fonts", "clean:images", "clean:script", "clean:tinymce"));

// Sass compiling
const sassOptions = {
  outputStyle: "compressed",
  lineNumbers: true,
};


gulp.task("sass", function () {
  gulp
    .src(srcTypographyScssFolder + "/**/*.scss")
    .pipe(concat("typography.scss"))
    .pipe(sass(sassOptions).on("error", sass.logError))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest(distCssFolder));

  return gulp
    .src(srcFolder + "/**/*.scss")
    .pipe(concat("styles.scss"))
    .pipe(sass(sassOptions).on("error", sass.logError))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest(distCssFolder));
});


// Copy assets from GOV UK frontend
function copyFactoryWithPattern(resourceName, sourceFolder, targetFolder, pattern) {
  return function () {
    return gulp
      .src(sourceFolder + pattern, {base: sourceFolder})
      .pipe(debug({"title": "Copy with pattern"}))
      .pipe(gulp.dest(targetFolder))
      .on("end", function () {
        console.log("📂  Copied " + resourceName);
        console.log("📂  Copied from " + sourceFolder + " into " + targetFolder);
      });

  };
}


// Copy assets from GOV UK frontend
function copyFactory(resourceName, sourceFolder, targetFolder) {
  return copyFactoryWithPattern(resourceName, sourceFolder, targetFolder, "/**/*");
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
  "copy:govuk_frontend_assets:scripts",
  copyFactoryWithPattern(
    "scripts from the GOVUK frontend assets",
    govukFrontendScriptsFolder,
    distScriptFolder,
      "/*.js"
  )
);

gulp.task(
  "copy:tinymce",
  copyFactoryWithPattern(
    "copy tinymce into a static folder",
    tinyMCERoot,
    distTinyMCEFolder,
      "/**/*"
  )
);

gulp.task(
  "copy:tinymce_langs",
  async function(){
    return gulp
      .src(tinyMCELangRoot + "/**/*", {base: tinyMCELangRoot})
      .pipe(debug({"title": "tinymce_langs"}))
      .pipe(gulp.dest(distTinyMCELangFolder))
    .on("end", function () {
        gulp
          .src(distTinyMCELangFolder + '/uk.js', { allowEmpty: true })
          .pipe(debug({"title": "create_uk_lang"}))
            .pipe(rename('en_GB.js'))
            .pipe(gulp.dest(distTinyMCELangFolder));

      });
  }
);

gulp.task(
  "copy:scripts_to_tinymce",
  copyFactoryWithPattern(
    "copy javascript into a static folder",
    srcScripts,
    distTinyMCEFolder,
      "/**/*"
  )
);

gulp.task(
  "copyAssets",
  gulp.parallel(
      "copy:govuk_frontend_assets:fonts",
      "copy:govuk_frontend_assets:images",
      "copy:govuk_frontend_assets:scripts",
      "copy:tinymce",
      "copy:tinymce_langs",
      "copy:scripts_to_tinymce"
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

