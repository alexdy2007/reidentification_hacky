$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/comparefile',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                for (i=0; i<data.length; i++){
                    console.log("----------------------------------");
                    console.log("Image : " + JSON.stringify(data[i][0]));
                    console.log("Distance : " + JSON.stringify(data[i][1]));
                }
            },
        });
    });

    function get_image(filenames){
        for(i=0; i<filenames.length; i++){
            file_name = filenames[0]
        }
    }
});