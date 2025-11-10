// Import the functions you need from the SDKs you need
  import { createUserWithEmailAndPassword, getAuth } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-analytics.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
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
  const submit = document.getElementById('submit');
  submit.addEventListener('click', function(event) {
    event.preventDefault();
    const auth = getAuth();
    const username = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    // ..
  });

  });