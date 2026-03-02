// wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', function() {
    // get subject dropdown element
    const subjectSelect = document.querySelector('select[name="subject"]');
    // get all tag label elements
    const tagLabels = document.querySelectorAll('.tag-badge.checkbox-label');
    // function to filter tags based on selected subject
    function filterTags() {
        // get selected subject
        const selectedSubject = subjectSelect.value;
        // loop through each tag label and show/hide based on whether it matches the selected subject
        tagLabels.forEach(function(label) {
            const subjects = label.getAttribute('data-subjects');
            if (!selectedSubject) {
                label.style.display = '';
            } else if (!subjects) {
                label.style.display = 'none';
            } else {
                const subjectList = subjects.split(',');
                if (subjectList.includes(selectedSubject)) {
                    label.style.display = '';
                } else {
                    label.style.display = 'none';
                }
            }
        });
    }

    if (subjectSelect) {
        subjectSelect.addEventListener('change', filterTags);
        filterTags(); // Initial filter on page load
    }
});