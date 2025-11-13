import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-auth.js";
import { doc, getDoc, getFirestore } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-firestore.js";
import { auth } from "/static/auth.js";
const db = getFirestore();
document.addEventListener('DOMContentLoaded', () => {
    onAuthStateChanged(auth, async(user) => {
    if (!user) {
        window.location.href = '/register';
        return;
    }

    const response = await getDoc(doc(db, "survey_responses", user.uid))
    if (!response.exists()) {
        return;
    }
    const responses = response.data();
    });
});

