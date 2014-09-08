define([
  'jquery',
  'underscore',
  'backbone',
  'views/ProjectList'
], function($, _, Backbone, ProjectListView, UserListView){

  var AppRouter = Backbone.Router.extend({
    routes: {
      // Define some URL routes
      '': 'home',
      // Default
      '*actions': 'defaultAction'
    }
  });

  var initialize = function(){
    var app_router = new AppRouter;

	  app_router.on('route:home', function(){
      // Call render on the module we loaded in via the dependency array
      // 'views/projects/list'
      var projectListView = new ProjectListView();
      projectListView.render();
      // console.log("Home Page working!");
    });

    app_router.on('route:defaultAction', function(actions){
      // We have no matching route, lets just log what the URL was
      console.log('No route:', actions);
    });

    Backbone.history.start();
  };

  return {
    initialize: initialize
  };

});