axios.get("http://192.168.27.4/move/forward");

setTimeout(() => {
  axios.get("http://192.168.27.4/rotate/right/90");
}, 5000);

setTimeout(() => {
  axios.get("http://192.168.27.4/move/forward");
}, 5500);

setTimeout(() => {
  axios.get("http://192.168.27.4/move/stop");
}, 10000);

setTimeout(() => {
  axios.get("http://192.168.27.4/block");
}, 11000);
