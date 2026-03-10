// wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', function() {
    // get subject dropdown element
    const subjectSelect = document.querySelector('select[name="subject"]');
    // get all tag label elements
    const tagLabels = document.querySelectorAll('.tag-badge.checkbox-label');
    // add checked class to label if input is checked
    tagLabels.forEach(function(label) {
        const input = label.querySelector('input[type="checkbox"]');
        if (input) {
            // initial state
            if (input.checked) {
                label.classList.add('checked');
            } else {
                label.classList.remove('checked');
            }
            // listen for change
            input.addEventListener('change', function() {
                if (input.checked) {
                    label.classList.add('checked');
                } else {
                    label.classList.remove('checked');
                }
            });
        }
    });
    // function to filter tags based on selected subject
    function filterTags() {
        const selectedSubjectId = subjectSelect.value;
        const tags = subjectTags[selectedSubjectId] || [];
        console.log('Selected subject ID:', selectedSubjectId);
        console.log('Available tags for subject:', tags);
        tagLabels.forEach(function(label) {
            const tagName = label.getAttribute('data-tag');
            console.log('Checking tag:', tagName, 'Visible:', !selectedSubjectId || tags.includes(tagName));
            if (!selectedSubjectId || tags.includes(tagName)) {
                label.style.display = '';
            } else {
                label.style.display = 'none';
            }
        });
    }

    if (subjectSelect) {
        subjectSelect.addEventListener('change', filterTags);
        filterTags(); // Initial filter on page load
    }
});