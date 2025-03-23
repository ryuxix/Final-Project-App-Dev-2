function showDescription(id) {
    // Hide all descriptions
    const descriptions = document.querySelectorAll('.description');
    descriptions.forEach(desc => desc.style.display = 'none');

    // Show the clicked description
    const description = document.getElementById(id);
    if (description) {
        description.style.display = 'block';
    }
}
