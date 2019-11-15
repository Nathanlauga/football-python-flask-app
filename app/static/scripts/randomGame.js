const randomGame = function() {
  function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }
  const select = document.getElementsByTagName("select");

  for (let s of select) {
    s.selectedIndex = getRandomInt(s.length) + 1;
  }
};
