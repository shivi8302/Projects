const coderProfiles = [
  {
    name: "Aria Blaze",
    image: "https://placekitten.com/400/300",
    bio: "Frontend firestarter. Brings pixels to life.",
    skills: ["HTML", "CSS", "JavaScript", "React"]
  },
  {
    name: "Max Quantum",
    image: "https://placebear.com/400/300",
    bio: "Data scientist in orbit. Powered by pandas & neural nets.",
    skills: ["Python", "NumPy", "Pandas", "R", "TensorFlow"]
  },
  {
    name: "Juno Sparks",
    image: "https://placebeard.it/400x300",
    bio: "Full-stack fusion reactor. API chef + UI designer.",
    skills: ["Node.js", "MongoDB", "HTML", "CSS", "JavaScript"]
  },
  {
    name: "Nova Linx",
    image: "https://placehold.co/400x300",
    bio: "Systems engineer who dreams in Rust.",
    skills: ["C", "C+", "C++", "Rust", "Go", "Linux"]
  },
  {
    name: "Echo Vega",
    image: "https://placekitten.com/400/301",
    bio: "AI whisperer optimizing galaxies one model at a time.",
    skills: ["Python", "Demongo", "Java", "Machine Learning", "Numpy"]
  }
];

let currentIndex = 0;
const card = document.getElementById('profileCard');
const profileImage = document.getElementById('profileImage');
const profileName = document.getElementById('profileName');
const profileBio = document.getElementById('profileBio');
const skillsList = document.getElementById('skillsList');
const chatSection = document.getElementById('chatSection');
const chatUser = document.getElementById('chatUser');
const friendsList = document.getElementById('friendsList');

function loadProfile(index) {
  const profile = coderProfiles[index];
  profileImage.src = profile.image;
  profileName.textContent = profile.name;
  profileBio.textContent = profile.bio;
  skillsList.innerHTML = "";
  profile.skills.forEach(skill => {
    const span = document.createElement("span");
    span.className = "skill";
    span.textContent = skill;
    skillsList.appendChild(span);
  });
}

loadProfile(currentIndex);

let startX, startY, currentX, currentY, isDragging = false;

card.addEventListener('mousedown', startDrag);
card.addEventListener('touchstart', startDrag);
document.addEventListener('mousemove', onDrag);
document.addEventListener('touchmove', onDrag);
document.addEventListener('mouseup', endDrag);
document.addEventListener('touchend', endDrag);

function startDrag(e) {
  isDragging = true;
  const point = e.type.startsWith('touch') ? e.touches[0] : e;
  startX = point.clientX;
  startY = point.clientY;
  card.style.transition = 'none';
}

function onDrag(e) {
  if (!isDragging) return;
  const point = e.type.startsWith('touch') ? e.touches[0] : e;
  currentX = point.clientX;
  currentY = point.clientY;
  const deltaX = currentX - startX;
  const deltaY = currentY - startY;
  card.style.transform = `translate(${deltaX}px, ${deltaY}px) rotate(${deltaX * 0.1}deg)`;
}

function endDrag() {
  if (!isDragging) return;
  isDragging = false;
  const deltaX = currentX - startX;
  const threshold = 100;

  if (deltaX > threshold) {
    // Swipe right = Interested
    openChat(coderProfiles[currentIndex].name);
    addToFriends(coderProfiles[currentIndex].name);
    nextProfile();
  } else if (deltaX < -threshold) {
    // Swipe left = Next
    nextProfile();
  } else {
    card.style.transition = 'transform 0.3s ease';
    card.style.transform = '';
  }
}

function nextProfile() {
  card.style.transition = 'transform 0.5s ease';
  card.style.transform = 'translateX(500px) rotate(20deg)';
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % coderProfiles.length;
    loadProfile(currentIndex);
    card.style.transition = 'none';
    card.style.transform = '';
  }, 500);
}

function openChat(name) {
  chatUser.textContent = name;
  chatSection.classList.add('section', 'show');
}

function closeChat() {
  chatSection.classList.remove('show');
}

function addToFriends(name) {
  const li = document.createElement('li');
  li.textContent = name;
  friendsList.appendChild(li);
}