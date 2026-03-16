/* global $, jQuery */
(function($) {
    "use strict";

    // ===========================
    // GLOBAL AJAX SETUP & CSRF
    // ===========================

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
        }
    });

    // Wrap code in jQuery ready handler to ensure $ is defined
    jQuery(function($) {
        
        // VARIABLES

        // get subject dropdown element
        const subjectSelect = $('select[name="subject"]');

        // get all tag label elements
        const tagLabels = $('.tag-badge.checkbox-label');

        // CHECKBOX TOGGLE HANDLER

        // add checked class to label if input is checked
        tagLabels.each(function() {
            const label = $(this);
            const input = label.find('input[type="checkbox"]');

            if (input.length) {
                // set initial state
                    label.toggleClass('checked', input.prop('checked'));

                // update class on change
                input.on('change', function() {
                    label.toggleClass('checked', input.prop('checked'));
                });
            }
        });

        // FILTER TAGS BASED ON SUBJECT

        // fetch tags for selected subject and show/hide tag labels
        function filterTagsAjax() {
            const selectedSubjectId = subjectSelect.val();

            // If no subject is selected, show all tags
            if (!selectedSubjectId || selectedSubjectId === 'null') { return; }

            // Fetch tags from the server
            fetch(`/get-subject-tags/?subject_id=${selectedSubjectId}`)
                .then(res => res.json())
                .then(data => {
                    const tags = data.tags || [];

                    // Loop over all tag labels and show/hide based on whether they belong to the selected subject
                    tagLabels.each(function() {
                        const label = $(this);
                        const tagName = label.data('tag'); // data-tag attribute
                        label.toggle(tags.includes(tagName)); // show if in tags
                    });
                })
                .catch(err => console.error('Error fetching tags:', err));
        }

        // Attach change event handler to subject dropdown
        if (subjectSelect.length) {
            subjectSelect.on('change', filterTagsAjax);

            // Run filter on page load in case a subject is pre-selected
            filterTagsAjax();
        }


        // ---------------------------
        // AJAX FORM SUBMISSION
        // ---------------------------
        $(document).on('submit', 'form.feed-filter-form, form.profile-filter-form, form.subject-filter-form', function(e) {
            e.preventDefault();
            const $form = $(this);
            $.ajax({
                url: $form.attr('action') || window.location.pathname,
                data: $form.serialize(),
                type: $form.attr('method') || 'GET',
                success: function(data) {
                    $('#feed-container').html(data);
                },
                error: function(xhr) {
                    alert('Error: ' + xhr.statusText);
                }
            });
        });

        // ---------------------------
        // LIKE BUTTON HANDLER (AJAX)
        // ---------------------------
        $(document).on('click', '.like-post-btn, .like-comment-btn, .like-resource-btn', function(e) {
            e.preventDefault();
            const $btn = $(this);
            const form = $btn.closest('form');
            $.ajax({
                url: form.attr('action'),
                type: 'POST',
                data: form.serialize(),
                success: function(data) {
                    const itemId = $btn.data('post-id') || $btn.data('comment-id') || $btn.data('resource-id');
                    if (itemId) {
                        $(`.post-like-count[data-post-id="${itemId}"], .post-like-count[data-comment-id="${itemId}"], .post-like-count[data-resource-id="${itemId}"]`).text(data.like_count);
                    }
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
    });
})(jQuery); // end IIFE