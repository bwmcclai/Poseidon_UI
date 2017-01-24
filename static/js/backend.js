function makeStatusCard(device, status, detail) {
    return '<div class="col-md-3"> \
                <div class="status-card text-center"> \
                    <h1>'+device+'</h1> \
                    <h3>'+status+'</h3> \
                    <h5>'+detail+'</h5> \
                </div> \
            </div>';
}

function getStatus() {
    $.ajax({
            url: '/getStatus',
            data: '',
            type: 'POST',
            contentType: 'application/json',
            success: function(response) {
                var html = '';
                for ( var i = 0 ; i < response.length ; i++ ) {
                    html += makeStatusCard(response[i]["device"],response[i]["status"],response[i]["detail"]);
                }
                document.getElementById('status-cards').innerHTML = html;
                console.log("Request status");
            },
            error: function(error) {
                console.log(error);
            }
        });
}

$(function() {
    $('#btnDoSomething').click(function() {
 
        $.ajax({
            url: '/doSomething',
            data: 'rusty=1',
            type: 'POST',
            success: function(response) {
                document.getElementById('btnDoSomething').text = 'Rusty'
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(function() {
    setInterval(getStatus, 1000);
});