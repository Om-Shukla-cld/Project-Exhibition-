// Registration captcha logic
let sRegAns = 0;
function genRegCaptcha() {
  const a = Math.floor(Math.random()*9)+1;
  const b = Math.floor(Math.random()*9)+1;
  const op = Math.random()<0.5 ? '+' : '×';
  sRegAns = op==='+' ? a+b : a*b;
  document.getElementById('sRegCaptchaText').textContent = `${a} ${op} ${b} = ?`;
}
document.querySelector('[data-open="studentRegister"]').addEventListener('click', genRegCaptcha);
document.getElementById('sRegCaptchaRefresh').addEventListener('click', genRegCaptcha);

document.getElementById('sRegDoneBtn').addEventListener('click', ()=>{
  const name = document.getElementById('sRegName').value.trim();
  const regNo = document.getElementById('sRegNo').value.trim();
  const captcha = document.getElementById('sRegCaptchaInput').value.trim();
  if(!name || !regNo || !captcha) {
    document.getElementById('sRegStatus').textContent = 'Please fill all fields.';
    document.getElementById('sRegStatus').style.color = '#ffb3b3';
    return;
  }
  if(Number(captcha) !== sRegAns) {
    document.getElementById('sRegStatus').textContent = 'Captcha incorrect.';
    document.getElementById('sRegStatus').style.color = '#ffb3b3';
    genRegCaptcha();
    return;
  }
  document.getElementById('sRegStatus').textContent = 'Registration successful! Redirecting...';
  document.getElementById('sRegStatus').style.color = '#cfe1ff';

  setTimeout(()=>{
    document.getElementById('studentRegister').classList.remove('active');
    openDash('studentDash');
    startCamera(); // <-- Start webcam after registration
    // Optionally clear fields
    document.getElementById('sRegName').value = '';
    document.getElementById('sRegNo').value = '';
    document.getElementById('sRegCaptchaInput').value = '';
    document.getElementById('sRegStatus').textContent = 'Demo only — no real backend attached.';
    document.getElementById('sRegStatus').style.color = '#cfe1ff';
  }, 1000);
});