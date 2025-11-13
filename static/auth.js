// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-app.js";
import { createUserWithEmailAndPassword, getAuth, signOut, updateProfile } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-auth.js";

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
  const auth = getAuth();
  document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM loaded");
    const submit = document.getElementById('submit');    
    if (!submit) {
        console.log("Submit button is null!");
        return;
    }
    console.log("Submit button:", submit);
    submit.addEventListener('click', function(event) {
    console.log("Button clicked!");
    event.preventDefault();
    const emailInput = document.getElementById('email1');
    const passwordInput = document.getElementById('password1');
    const nameInput = document.getElementById('name');
    const email = emailInput.value;
    const name = nameInput.value;
  const password = passwordInput.value;
createUserWithEmailAndPassword(auth, email, password)
  .then(async (userCredential) => {
    const user = userCredential.user;
    emailInput.value = '';
    passwordInput.value = '';

    try {
      await updateProfile(user, { displayName: name });
      console.log("Display name set:", user.displayName); 
      nameInput.value = '';
    } catch (err) {
      console.error("Failed to set display name:", err);
    }
    window.location.href = '/survey';
  })
  .catch((error) => {
    const errorCode = error.code;
    if (errorCode == 'auth/email-already-in-use') {
      alert('Email is taken');
      emailInput.value = '';
      passwordInput.value = '';
      nameInput.value = '';
    }
    else if (errorCode == 'auth/invalid-email') {
      alert('Not a valid email');
      emailInput.value = '';
      passwordInput.value = '';
      nameInput.value = '';
    }
    else if (errorCode == 'auth/weak-password') {
      alert('Password is too short');
      emailInput.value = '';
      passwordInput.value = '';
      nameInput.value = '';
    }
    else if (errorCode == 'auth/missing-email') {
      alert('Please enter a valid email');
      emailInput.value = '';
      passwordInput.value = '';
      nameInput.value = '';
    }
    else {
      alert('Something went wrong. Please try again later');
      emailInput.value = '';
      passwordInput.value = '';
      nameInput.value = '';
    }
  });
  
  });
  });
export function logout() {
  signOut(auth).then(() => {
    window.location.href = "/landing";
  }).catch((error) => {
    console.error("Logout failed:", error);
  });
};
export { auth };
