var countdown_min;

var shortEvent = document.getElementById("short-break");
if (shortEvent) {
    countdown_min = 5;
}

var longEvent = document.getElementById("long-break");
if (longEvent) {
    countdown_min = 15;
}

var endEvent = document.getElementById("end-submit");
if (endEvent) {
    countdown_min = 0;
}
    
var pomodoroEvent = document.getElementById("long-break");
if (pomodoroEvent) {
    countdown_min = 25;
}

var now = new Date().getTime();
var countDownDate = new Date(now + countdown_min*60000);

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("showtime").innerHTML = minutes + ":" + seconds;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("showtime").innerHTML = "EXPIRED";
  }
}, 1000);