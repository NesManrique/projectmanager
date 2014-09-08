define(function (require) {
    var $ = require('jquery'),
        _ = require('underscore');
		Backbone = require('backbone');

    var Projects = Backbone.Collection.extend({

    	url:'/api/projects/',
    	toJSON: function(options){
    		return this.models[0].get('results');
    	}
    });

    return Projects;
});