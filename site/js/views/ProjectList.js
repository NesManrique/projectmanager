define(function (require) {
    var $ = require('jquery'),
        _ = require('underscore');
		Backbone = require('backbone');
		Projects = require('collections/Projects');
		projectListT = require('text!templates/project_list.html');
    var ProjectListView = Backbone.View.extend({
    	el: '.page',
    	render: function(){
    		var that = this;
    		var projects = new Projects();
    		projects.fetch({
    			success: function(projects){
    				var template = _.template(projectListT,{projects: projects.toJSON()});
    				that.$el.html(template);		
    			}
    		});
    	}

    });

    return ProjectListView;
});