// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-app.js";
import { doc, getFirestore, setDoc } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-firestore.js";
import { auth } from "/static/auth.js";


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
  const db = getFirestore(app);
document.addEventListener("DOMContentLoaded", () =>{
    const submit = document.getElementById('submit');
    const slides = document.querySelectorAll('.q');
    let currentSlide = 0;
    const showSlide = (index) => {
        slides.forEach  ((s,i) => s.classList.toggle('active',i===index));
    };
    document.querySelectorAll('.next').forEach(btn => {
        btn.addEventListener('click', () => {
            if(currentSlide <slides.length-1) {
                currentSlide++;
                showSlide(currentSlide);
            }
        });
    });

    document.querySelectorAll('.back').forEach(btn => {
        btn.addEventListener('click', () => {
            if(currentSlide > 0) {
                currentSlide--;
                showSlide(currentSlide);
            }
        });
    });

    submit.addEventListener('click', async (event) => {
        event.preventDefault();
        const user = auth.currentUser;
        if (!user) {
            console.log('not logged in');
            return;
        }
        const categories = Array.from(document.querySelectorAll('input[name="categories"]:checked')).map(cb=>cb.value);
        const events = Array.from(document.querySelectorAll('input[name="event"]:checked')).map(cb=>cb.value);
        const interests = Array.from(document.querySelectorAll('input[name="interest"]:checked')).map(cb=>cb.value);
        const docRef = doc(db, 'survey_responses', user.uid);
        const response = {
            name: user.displayName,
            email: user.email,
            categories: categories,
            events: events,
            interests: interests
        }
        try {
            await setDoc(docRef, response);
            console.log('logged survey responses!');
             window.location.href = '/dashboard';
        } catch (err) {
            console.log('Error writing document: ', err);
        }

    });
});

