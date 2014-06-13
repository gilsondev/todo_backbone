module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // JsHint
    jshint: {
        all: ['js/**/*.js']
    },

    // Watch
    watch: {
        scripts: {
            files: ['js/**/*.js'],
            tasks: ['jshint']
        },
        css: {
            files: ['css/**/*.css']
        }
    }
  });

  // Load plugins
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['jshint']);
};
