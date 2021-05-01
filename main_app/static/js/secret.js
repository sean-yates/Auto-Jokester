// Thanks StackOverflow!

const correctKeys = {
    72: 'h'
    65: 'a',
  };
  
  const secretCode = ['h', 'a', 'h', 'a', 'h', 'a'];
  
  var codePosition = 0;
  
  document.addEventListener('keydown', function(e) {
    let key = allowedKeys[e.keyCode];
    let requiredKey = secretCode[codePosition];
  
    if (key == requiredKey) {

      codePosition++;
  
      if (codePosition == secretCode.length) {
        activateCheats();
        codePosition = 0;
      }
    } else {
      codePosition = 0;
    }
  });
  
  function activateCheats() {
    // document.body.style.backgroundImage = "url('images/cheatBackground.png')";
  
    // var audio = new Audio('audio/pling.mp3');
    // audio.play();
  
    alert("cheats activated");
  }