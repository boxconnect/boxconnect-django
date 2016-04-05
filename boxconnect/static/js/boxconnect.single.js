(function($) {
	$('#btnBoxconnect').click(function() {
		options = {
		    success: function(files) {
		    	var data = {files: files, action: "saveFiles"};
				$.ajax({
				    type: "POST",
				    url: "",
				    data: data,
				    dataType: "json",
				    success: function(data){
				    	var hidden = $('div.bc-hidden');
				    	$(hidden).removeClass('bc-hidden');
						$('html, body').animate({scrollTop: $(hidden).first().offset().top}, 1000);

				    }
				});
		    },
		    linkType: "direct",
		    multiselect: true
		};
		Dropbox.choose(options);
	});
}(jQuery));