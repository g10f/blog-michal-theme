const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');
const rename = require("gulp-rename");
const {parallel} = require('gulp');

const config = {
    srcCss: ['./michal_theme/static/scss/michal.scss'], buildCss: './michal_theme/static/css'
};

function buildStyles() {
    return gulp.src(config.srcCss)
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(config.buildCss))
}

function buildMinStyles() {
    return gulp.src(config.srcCss)
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(rename({extname: '.min.css'}))
        .pipe(gulp.dest(config.buildCss))
}


exports.default = parallel(buildStyles, buildMinStyles);
