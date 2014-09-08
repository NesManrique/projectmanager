// Filename: main.js

// Require.js allows us to configure shortcut alias
// There usage will become more apparent further along in the tutorial.
require.config({
  paths: {
    jquery: 'libs/jquery/jquery-1.11.0',
    underscore: 'libs/underscore/underscore',
    backbone: 'libs/backbone/backbone',
    sbadmin: 'libs/bootstrap/sb-admin-2',
    //datatables: 'libs/plugins/dataTables/jquery.dataTables',
    bootstrap: 'libs/bootstrap/bootstrap.min',
    //datatablesbootstrap: 'libs/plugins/dataTables/dataTables.bootstrap',
    //flot: 'libs/plugins/flot/',
    metisMenu: 'libs/plugins/metisMenu/metisMenu.min',
    //morris: '/libs/plugins/morris/'
  },
  shim: {
	'backbone': {
        //These script dependencies should be loaded before loading
        //backbone.js
        deps: ['underscore', 'jquery'],
        //Once loaded, use the global 'Backbone' as the
        //module value.
        exports: 'Backbone'
    },
    /*'bootstrap': {
        deps: ['jquery'],
        exports: 'Bootstrap'
    },
    'metisMenu': {
        deps: ['jquery','bootstrap'],
        exports: ['MetisMenu']
    },
    'sbadmin': {
        deps: ['jquery','bootstrap','metisMenu'],
        exports: 'Sbadmin'
    },*/
    'underscore': {
        exports: '_'
    }
  }
});

require([
  // Load our app module and pass it to our definition function
  'projectManager',
  'jquery',
  'underscore',
  'backbone',
  /*'bootstrap',
  'metisMenu',
  'sbadmin'*/
], function(ProjectManager){
  // The "app" dependency is passed in as "App"
  ProjectManager.initialize();
});