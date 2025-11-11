// Import the functions you need from the SDKs you need
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-analytics.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-auth.js";
document.addEventListener("DOMContentLoaded", () => {
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyDeYP4-IDnXT9wQxUW2jB63efAyaM8aqtI",
    authDomain: "community-resource-auth.firebaseapp.com",
    projectId: "community-resource-auth",
    storageBucket: "community-resource-auth.firebasestorage.app",
    messagingSenderId: "237984021975",
    appId: "1:237984021975:web:3a5634370c0023fdba5f92",
    measurementId: "G-08V3PE9467"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
  const login = document.getElementById('login');
  login.addEventListener('click', function(event) {
    event.preventDefault();
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const auth = getAuth();
    const email = emailInput.value;
  const password = passwordInput.value;
  signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    window.location.href = '/dashboard'
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    console.log(error)
    let message = '';
      if (errorCode.includes('user-not-found')) {
        message = 'No account found with this email';
    } else if (errorCode.includes('wrong-password')) {
        message = 'Incorrect password';
    } else if (errorCode.includes('invalid-email')) {
        message = 'Not a valid email';
    } else {
         message = 'Something went wrong. Please try again later';
    }
    alert(message);
    emailInput.value = '';
    passwordInput.value = '';
  });

  });

});