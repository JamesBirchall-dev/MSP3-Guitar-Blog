// wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', function() {
        // AJAX handler for filter form submit
        const filterForm = document.querySelector('form.card');
        if (filterForm) {
            filterForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const params = new URLSearchParams(new FormData(filterForm)).toString();
                fetch('?' + params, {
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                })
                .then(response => response.text())
                .then(html => {
                    document.getElementById('feed-container').innerHTML = html;
                });
            });
        }
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
    // function to filter tags based on selected subject using AJAX
    function filterTagsAjax() {
        const subjectSelect = document.querySelector('select[name="subject"]');
        const selectedOption = subjectSelect.options[subjectSelect.selectedIndex];
        const selectedSubjectId = selectedOption.getAttribute('data-pk');
        fetch(`/get-subject-tags/?subject_id=${selectedSubjectId}`)
            .then(response => response.json())
            .then(data => {
                const tags = data.tags || [];
                tagLabels.forEach(function(label) {
                    const tagName = label.getAttribute('data-tag');
                    if (!selectedSubjectId || tags.includes(tagName)) {
                        label.style.display = '';
                    } else {
                        label.style.display = 'none';
                    }
                });
            });
    }
    
        if (subjectSelect) {
            subjectSelect.addEventListener('change', filterTagsAjax);
            const selectedOption = subjectSelect.options[subjectSelect.selectedIndex];
            const selectedSubjectId = selectedOption && selectedOption.getAttribute('data-pk');
            if (selectedSubjectId && selectedSubjectId !== 'null') {
                filterTagsAjax();
            }
        }
});


$(document).ready(function() {

    // get subject dropdown element
    const subjectSelect = $('select[name="subject"]');

    // get all tag label elements
    const tagLabels = $('.tag-badge.checkbox-label');

    // add checked class to label if input is checked
    tagLabels.each(function() {
        const label = $(this);
        const input = label.find('input[type="checkbox"]');

        if (input.length) {
            if (input.prop('checked')) {
                label.addClass('checked');
            } else {
                label.removeClass('checked');
            }

            input.on('change', function() {
                if (input.prop('checked')) {
                    label.addClass('checked');
                } else {
                    label.removeClass('checked');
                }
            });
        }
    });
    });
    // function to filter tags based on selected subject
    function filterTags() {
        const selectedSubjectId = subjectSelect.val();
        const tags = window.subjectTags[selectedSubjectId] || [];

        tagLabels.each(function() {
            const label = $(this);
            const tagName = label.data('tag');

            if (!selectedSubjectId || tags.includes(tagName)) {
                label.show();
            } else {
                label.hide();
            }
        });
    }

    function filterTagsAjax() {
        const selectedSubjectId = subjectSelect.value;
        if (!selectedSubjectId || selectedSubjectId === 'null') {
            // Do not make AJAX call if subject_id is invalid
            return;
        }
        fetch(`/get-subject-tags/?subject_id=${selectedSubjectId}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const tags = data.tags || [];
                tagLabels.forEach(function(label) {
                    const tagName = label.getAttribute('data-tag');
                    if (!selectedSubjectId || tags.includes(tagName)) {
                        label.style.display = '';
                    } else {
                        label.style.display = 'none';
                    }
                });
            })
            .catch(error => {
                console.error('Error fetching tags:', error);
            });
    }

    // -------------------------
    // AJAX FORM HANDLER
    // -------------------------

    // Restrict AJAX handler to feed/filter forms only
    $('form.feed-filter-form, form.profile-filter-form, form.subject-filter-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: window.location.pathname,
            data: $(this).serialize(),
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function(data) {
                $('#feed-container').html(data);
            }
        });
    })

    // Click event for like buttons
    $(document).on('click', '.like-post-btn', function(e) {
    e.preventDefault();
    var $btn = $(this);
    var form = $btn.closest('form');
    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: form.serialize(),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        success: function(data) {
            // Update like count for post
            var postId = $btn.data('post-id');
            if (postId) {
                $('.post-like-count[data-post-id="' + postId + '"]').text(data.like_count);
            }
            // Update like count for resource
            var resourceId = $btn.data('resource-id');
            if (resourceId) {
                $('.post-like-count[data-resource-id="' + resourceId + '"]').text(data.like_count);
            }
            // Update like count for comment
            var commentId = $btn.data('comment-id');
            if (commentId) {
                $('.post-like-count[data-comment-id="' + commentId + '"]').text(data.like_count);
            }
            // Update icon
            if (data.liked) {
                $btn.find('i').removeClass('far').addClass('fas text-danger');
            } else {
                $btn.find('i').removeClass('fas text-danger').addClass('far');
            }
        },
        error: function(xhr) {
            alert('Error: ' + xhr.statusText);
        }
    });
});
