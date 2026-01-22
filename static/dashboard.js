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
    
    async function custom_dash() {
    const response = await fetch('/data/resources', { method: 'GET' });
    const allResources = await response.json();
    return allResources
    }
    const categoryMap = {
        "Education": "Education & Youth",
        "Health": "Health & Wellness",
        "Safety": "Social Services & Support",
        "Parks": "Environmental & Sustainability",
        "Art": "Arts, Culture, & Recreation",
        "Volunteering": "Community Events & Volunteering"
    }
    const resources = await custom_dash();
    const userCategories = responses.categories || [];
    const resources_categories = userCategories.map(category => {
        return categoryMap[category];
    }).filter(Boolean);
    const filtered_resources = resources.filter(resource => {
       return resources_categories.includes(resource.category);
        });
    const tagMap = {
        "STEM": ["STEM", "STEAM","technology", "programming"],
        "Art": ["arts","culture", "museum"],
        "Health": ["health", "wellness", "primary_care", "family_health"],
        "Community-service": ["volunteering", "gardening", "community", "families"]
    }
    const allowedTags = [];
    const userTags = responses.interests;
    userTags.forEach(tag => {
        if (tagMap[tag]) {
        allowedTags.push(...tagMap[tag]);
        }
    });
    const filtered_tags = filtered_resources.filter(resource => {
        return resource.tags.some(tag => allowedTags.includes(tag));
    });
    const finalResources = filtered_tags.length > 0 
    ? filtered_tags 
    : resources;
    const container = document.getElementById('resources-container');
    container.innerHTML = '';
    finalResources.sort(() => Math.random() - 0.5).slice(0, 5).forEach(resource => {
        const card = document.createElement('div');
        card.className = "flex flex-none flex-col h-[70vh] bg-white rounded-2xl w-[45%] rounded-lg cursor-pointer hover:shadow-lg transition";
        card.dataset.url = `/resource/${resource.id}`; 
        card.innerHTML =  `
        <img src="static/images/${resource.img}" class="object-cover rounded-t-2xl w-full h-[55%] mb-3">
        <div class="flex flex-col px-4">
            <div class="flex flex-row items-center gap-4 mb-2">
                <h2 class="heading-font font-base">${resource.name}</h2>
            </div>
            <p class="body-font font-sm font-light">${resource.description}</p>
            <div class="mt-3 flex flex-row gap-2">
                ${resource.tags.slice(0,2).map(tag => `
                    <div class="bg-gray-200 text-gray-800 text-xs px-2 py-1 rounded-full flex flex-row items-center gap-2">
                        <img src="/static/images/tag.png" alt="Tag Icon" class="w-auto h-3">
                        ${tag}
                    </div>
                `).join('')}
            </div>
        </div>
        `;
    card.addEventListener('click', function(){
        window.location.href = card.dataset.url;
    });
    container.appendChild(card);

    });
    
   });
    });



