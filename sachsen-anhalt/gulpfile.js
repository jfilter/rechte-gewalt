var gulp = require('gulp');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');


var concat = require('gulp-concat');
 
gulp.task('default', function() {
  return gulp.src(['./bower_components/jquery/dist/jquery.min.js', './bower_components/raphael/raphael-min.js', './bower_components/kartograph.js/kartograph-0.8.2.min.js', './lib/file2.js', './bower_components/bootstrap/dist/js/bootstrap.min.js', './bower_components/qtip2/jquery.qtip.min.js'])
    .pipe(concat('all.js'))
    .pipe(gulp.dest('./'));
});

gulp.task('min', function() {
	return gulp.src('script.js')
		.pipe(uglify())
		.pipe(rename({ suffix: '.min' }))
		.pipe(gulp.dest('./'))
})