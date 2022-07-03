let video = document.getElementById('videoElement');

if(navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true})
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.log("Error: " + err);
    });
} else {
    console.log("getUserMedia not supported");
}