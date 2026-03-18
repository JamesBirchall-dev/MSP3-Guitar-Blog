# Guitar-Learning-Blog

![device view](/static/images/readmeimages/guitairblog-devices.png)

## Table of Contents

- Project Rationale & Purpose
- Target Audience
- Features Overview
- UX & Accessibility
- Data Schema & Configuration
- Testing Procedures
- Deployment Instructions
- Security Features
- Development Process
- Attribution
- Screenshots & Demo
- Known Issues & Future Improvements

---

## Project Rationale & Purpose

As someone who has both taught guitar and learned independently, I have found that platforms such as YouTube provide an enormous amount of valuable content but can also be overwhelming for beginners and intermediate learners. With many different teachers, teaching philosophies, and lesson structures available, learners can often end up "going down rabbit holes" of content without developing a balanced or structured learning progression. This can lead to knowledge gaps in key areas such as technique, theory, or practice structure.

The goal of this project is to develop a community-driven guitar learning platform where teachers can publish structured learning posts in clearly defined subjects. Other users can participate by discussing the posts and sharing additional learning resources such as videos, articles, or tablature.

The site combines elements of a blog, forum, and collaborative resource hub, allowing learners to discover structured lessons while benefiting from community recommendations and discussion.

Content is organised into subjects and tags, and users can filter the feed to discover relevant content. A teacher-level role acts as a moderator layer, with the ability to verify community-submitted resources, helping highlight high-quality learning materials.

Users can also like posts, comments, and resources, allowing the most helpful contributions to surface within the community.

## Target Audience

The 2 main distinct user profiles/roles for this site is Teacher vs Student, student being split into: Beginner, intermediate and advanced. Which will be part of the users' profile.

Teacher will only be asigned by admin through application to ensure learning content is moderated and to protect brand integrity.

The teacher profile would be experienced teachers and/or content creators who want to provide continued content, this will allow them to cross promote their existing social media channels.

The students will be self learning people interested in learning the instrument in a structured and thorough way, traffic mainly coming through the existing teachers existing channels and recommendations.

## Features Overview

The platform is designed as a structured, subject based guitar learning community where different levels of users interact through posts, comments and shared learning resources. The User Journey ensures intuitive navigation, clear content organisation and meaniningful engagement via the contribution system.

- CRUD for posts, comments, resources
- Authentication & user profiles
- Likes/voting system
- Resource verification by teachers
- Filtering, search, pagination
- AJAX updates for dynamic UX
- Responsive design

### CRUD for profile, posts, comments and resources

Posts

- Create: Teachers can create new posts (/create/, create_post view).
- Read: All users can view posts and their details (/post/<slug>/, post_detail view).
- Update: Authors can edit their posts (/post/<slug>/edit/, edit_post view).
- Delete: Authors can delete their posts (/post/<slug>/delete/, delete_post view).

Comments

- Create: Users can add comments to posts (handled in post_detail view).
- Read: Comments are displayed under posts.
- Update: Users can edit their own comments (/comment/<id>/edit/, edit_comment view).
- Delete: Users can delete their own comments (/comment/<id>/delete/, delete_comment view).

Resources

- Create: Users can share resources under posts or comments.
- Read: Resources are shown with posts/comments and in subject feeds.
- Update: Contributors can edit their resources (/resource/<id>/edit/, edit_resource view).
- Delete: Contributors can delete their resources (/resource/<id>/delete/, delete_resource view).
- Verify: Teachers can mark resources as verified (/verify-resource/<id>/, verify_resource view).

Profiles

- Create: Profile is created at user registration.
- Read: Profile pages show user info, posts, and resources (/profile/<username>/, profile_view).
- Update: Users can edit their profile (/profile/edit/, edit_profile view).
- Delete: Not directly exposed (users can delete their account via Django admin or custom logic).

### Authentication & user profiles

Authentication

- Register: Users can sign up with email, password, and select a skill level/role. Registration creates a user and associated profile. (URL: /register/)
- Login: Users log in using Django's authentication form. (URL: /login/)
- Logout: Users can log out, ending their session. (URL: /logout/)
- Role Assignment: During registration, users select a role (Beginner, Intermediate, Advanced, Teacher). Teacher role is restricted/admin-assigned.

User Profiles

- Profile Creation: Automatically created at registration, stores user info and role.
- Profile View: Each user has a profile page showing their info, posts, and resources. (URL: /profile/<username>/)
- Profile Edit: Users can update their profile details (bio, skill level, etc.). (URL: /profile/edit/)
- Role-based Permissions: Teachers can create posts and verify resources; students can comment, share resources, and vote.
- Reputation Stats: Profiles track likes/votes given and received, building user reputation.
- Filtering: Profile pages allow filtering by subject, tags, and search.

### Likes/voting system

- Posts: Users can like or unlike posts. Users cannot like their own posts. Like counts are updated dynamically via AJAX. (URL: /like-post/<id>/)
- Comments: Users can like or unlike comments. (URL: /like-comment/<id>/)
- Resources: Users can like or unlike shared resources. (URL: /like-resource/<id>/)
- Feedback: Like actions provide instant feedback and update the UI without page reloads.
- Reputation: Likes contribute to user reputation, tracked in their profile.
- Ranking: Content (posts, comments, resources) is sortable by like count and creation date to highlight the most useful contributions.
- Permissions: Only authenticated users can vote; users cannot vote on their own content.

### Resource verification by teachers

- Purpose: Allows teachers to mark community-submitted resources as "verified," highlighting high-quality learning materials.
- Who can verify: Only users with the "teacher" role have permission to verify resources.
- Verification Action: Teachers access a dedicated URL (/verify-resource/<id>/) to mark a resource as verified.
- UI Feedback: Verified resources are visually distinguished in the UI (e.g., badge or highlight), signaling trustworthiness to learners.

- Workflow:
- A student or teacher submits a resource under a post or comment.
- Teachers review resources and can verify them if they meet quality standards.
- Once verified, the resource is flagged in the database and shown as verified in feeds and post details.
- Moderation: Verification acts as a moderation layer, helping surface the best learning materials and maintain content quality.

### Filtering, search, sort & pagination

Filtering

- Users can filter content (posts, resources, comments) by subject, tags, and skill level.
- Filtering options are available on the homepage, subject feeds, and profile pages.
- AJAX endpoints dynamically update available tags when a subject is selected, improving UX.

Search

- Users can search for posts, resources, or subjects using keywords.
- Search results are displayed in feeds and can be combined with filtering for precise navigation.
- Search supports partial matches and is integrated with filtering and sorting.

Sort

- Content (posts, comments, resources) can be sorted by like count, creation date, or other criteria.
- Sorting helps users find the most relevant or popular content quickly.

Pagination

- Content feeds (posts, comments, resources) are paginated to improve performance and usability.
- Users can navigate between pages of results, ensuring manageable content loads.
- Pagination is applied to main feeds, subject feeds, and profile activity lists.

### AJAX updates for dynamic UX

- Like/Voting: Likes on posts, comments, and resources are processed via AJAX, instantly updating counts and UI without page reloads.
- Filtering: Tag options update dynamically when a subject is selected, using AJAX endpoints for a seamless filtering experience.
- Search: Search results and filtering are updated in real-time, allowing users to refine queries and see results instantly.
- Resource Verification: Verification actions by teachers update the resource status in the UI immediately.
- Commenting: New comments and resources can be submitted and displayed without reloading the page.
- Feedback: AJAX is used for error/success messages, providing immediate user feedback.
- Performance: Reduces full-page reloads, improving speed and responsiveness across the site.

### Responsive design

- Mobile-first layout: The site uses a mobile-first approach, ensuring usability on phones, tablets, and desktops.
- Flexible grids: Content is organized with CSS flexbox and grid layouts, adapting to different screen sizes.
- Adaptive navigation: Menus, filters, and forms adjust for touch and small screens, providing easy access and readability.
- Scalable images: Images and media scale automatically to fit device width, maintaining clarity and performance.
- Accessible controls: Buttons, links, and interactive elements remain usable and visible across all devices.
- Consistent experience: All features (filtering, search, voting, commenting) are fully functional on any device.

## UX & Accessibility

UX (User Experience)

- Clear navigation: Subjects, tags, and feeds are organized for intuitive browsing.
- User journeys: Designed for first-time visitors, students, teachers, and returning users, with tailored flows for each.
- Quick onboarding: Registration is simple, with clear prompts and feedback.
- Dynamic feedback: Actions (like, comment, verify) provide instant UI updates and success/error messages.
- Content ranking: Helpful content is surfaced via likes and teacher verification.

Accessibility

- Keyboard navigation: All interactive elements are accessible via keyboard.
- Semantic HTML: Uses proper HTML tags for structure and screen reader compatibility.
- Contrast & font size: Ensures readable text and visible controls for all users.
- Alt text: Images include descriptive alt attributes for screen readers.
- Responsive controls: Buttons, links, and forms are large and easy to interact with on any device.

### First Time Visitor

Journey

1. Lands on the homepage.
2. Browses subjects from the subject list.
3. Selects a subject.
4. Views posts by subject.
5. Opens a post.
6. Reads comments and shared resources.
7. Registers to participate in community.

Value:

1. Clear subject organisation and orientation.
2. Ranked comments with upvote system and teacher verification.
3. Quick onboarding via register form.

### Registered Student (Role: Beginner - Advanced)

Journey:

1. Logs into account
2. Reads recent posts via homefeed
3. Navigates or filters to subject for posts and resources.
4. leaves comment and optionally shares resources for posts.
5. votes on helpful resources.
6. See's own profile for their contribution.

Value:

1. Ability to contribute knowledge
2. Ability to provide feedback through comments and voting.
3. Can build profile reputation through displayed activity.

### Teacher User

(Can publish learning posts)

1. log into account
2. Create a new post
3. Assign a subject to post with any relevant tags
4. Publish post
5. Engages with students comments and resources.
6. Moderates and monitors resources shared under their posts.

### Returning User

For continued learning.

Journey:

1. Logs in
2. Returns to subject or feed
3. Filters chosen subject and tags
4. Views resources.

Value:

1. Structured navigation.
2. Dynamic filtering
3. Ranked content

## Data Schema & Configuration

- Data model diagram

![relationship diagram](/static/images/readmeimages/readme-data-relationship-diagram.png)

### Data Entity Relationship Table

The following table outlines the main entities used in the application, their key attributes, and how they relate to other entities within the database.

Corrected Table
| Entity | Key Fields | Relationships | Description |
| --- | --- | --- | --- |
| **User** | id, username, email, password | One-to-One with Profile | Django's built-in authentication model used to manage user accounts and login credentials. |
| **Profile** | id, user, role, bio | One-to-One with User | Extends the default Django user model to include additional information such as skill level and biography. Determines whether a user has teacher privileges. |
| **Subject** | id, name, slug, description | One-to-Many with Post<br>One-to-Many with Resource | Represents a high-level learning category (e.g. Practice, Theory, Songs). Used to organise posts and resources. |
| **Tag** | id, name, slug | Many-to-Many with Post | Provides more granular classification of posts within subjects. Enables filtering and search. |
| **Post** | id, title, slug, content, author, subject, min_level, created_at | Many-to-One with User (author)<br>Many-to-One with Subject<br>Many-to-Many with Tag<br>One-to-Many with Comment<br>One-to-Many with Resource | Represents the main learning content published by teachers. Posts act as discussion threads where users can comment and share resources. |
| **Comment** | id, content, author, post, created_at | Many-to-One with User<br>Many-to-One with Post<br>One-to-Many with Resource | Represents user discussion responses to posts. Comments can also contain shared learning resources. |
| **Resource** | id, title, url, description, contributor, verified, created_at | Many-to-One with User<br>Many-to-One with Post (optional)<br>Many-to-One with Comment (optional)<br>Many-to-One with Subject | Represents external learning materials such as videos, articles, or tablature. Resources may be attached to posts or comments. |
| **Like** | id, user, post, comment, resource | Many-to-One with User<br>Optional relation to Post, Comment, or Resource | Implements the voting system allowing users to like posts, comments, or resources. A validation rule ensures only one target is selected per like. |

## Relationship Overview

The relationships between entities are designed to support **collaborative learning and content discovery**.

### User Relationships

- A **User** has **one Profile**
- A **User** can create:
  - many Posts
  - many Comments
  - many Resources
  - many Likes

---

### Content Structure

The learning content structure follows a hierarchical pattern:

Subject\
 └── Post\
 └── Comment\
 └── Resource (optional)

Resources may also be attached directly to posts.

---

### Tagging System

Posts can belong to multiple tags:

Post\
 ↔ Tag

This many-to-many relationship allows flexible filtering and topic grouping.

---

### Voting System

The Like model supports engagement across multiple content types.

User\
 └── Like\
 ├── Post\
 ├── Comment\
 └── Resource

Each like is associated with only **one target object**, enforced by model validation.

---

### Summary

The data model supports the following key platform behaviours:

- **Structured learning content** through teacher-created posts
- **Community discussion** through comments
- **Collaborative resource sharing**
- **Content discovery through subjects and tags**
- **Community feedback via likes**
- **Quality control through teacher resource verification**

## Architechture Overview

### Application Architecture

The application used the Django Model View Template structure.

- Models define the database schema and relationships.
- Forms manager user input and validation.
- Views process requests, apply logic and return response.
- URLs route incoming requests to relevant views.

The platform functions as a community based guitar learning forum, combining structured teaching posts with discussion, shared resources and votes/ likes.

## Models

Models define the database stucture and the relationship between users, content and interactions.

### Subject

A high level category of learning content. Used for organising posts and resources.

Examples:

- Practise
- Theory
- Equipment
- Songs

Each subject includes:

- Name
- Slug
- Short Description for listing
- Full Description for detail
- Associated tags

### Tag

Tags provide more granullar classification than subjects.

Examples:

- Chords
- Fingerstyle
- Improvisation

Posts may have multiple tags to enable flexible filtering.

### Profile

The Profile model extends Djangos built in User model.

Stores additional information:

- User skill level (role)
- Bio
- Reputation statistics (likes/votes given/received)

Roles:

- Beginner
- Intermediate
- Advanced
- Teacher

Teachers have aditional permissions such as creating posts and verifying resources.

### Post

The Post model represents the main learning content created by teachers.

Each post includes:

- title
- slug
- author
- subject category
- tags
- content
- minimum skill level requirement
- publication status
- creation timestamp

Posts serve as the primary discussion threads where users can comment and share resources.

### Comment

The Comment model allows users to participate in discussion under posts.

Each comment stores:

- associated post
- author
- content
- creation timestamp
- approval status

Comments support collaborative learning and may also include attached learning resources.

### Resource

Resources represent external learning materials shared by users.

- YouTube tutorials
- blog articles
- instructional PDFs

May be assigned to:

- Posts
- Comments

Each resource stores:

- title
- URL
- description
- contributor
- associated subject
- verification status
- creation timestamp

Teachers can mark resources as verified to highlight high-quality learning material.

### Like

The Like model implements a flexible voting system.

Users may like:

- posts
- comments
- resources

Each like stores:

- the user who cast the vote
- the target object
- timestamp

A validation rule ensures that only one target type can be selected per like, and a uniqueness constraint prevents duplicate likes.

## Forms

Forms handle user input and validation before saving to the database.

### Register Forms

Extends Django’s built-in UserCreationForm.

Additional fields include:

- email
- skill level/ role

### PostForm

Used for creating and editing learning posts.

Fields include:

- title
- slug
- content (edited using Summernote rich text editor)
- minimum skill level
- subject
- tags

If no subject is selected when creating a post, the form attempts to default to **"Uncategorized"**.

### CommentForm

Allows users to submit comments under posts.

The form also includes optional fields allowing users to attach a resource when posting a comment.

Optional resource fields include:

- resource title
- resource URL
- resource description

A validation method ensures URLs include a proper protocol.

---

### ResourceForm

Used for creating or editing learning resources.

Fields include:

- title
- URL
- description

URL validation ensures external links are correctly formatted.

---

### ProfileForm

Allows users to update their profile information.

Editable fields include:

- skill level
- biography

The **teacher role is intentionally excluded** from the form to prevent users from granting themselves elevated permissions.

## Views

Views contain the core application logic and coordinate interactions between models, forms, and templates.

---

### Feed Views

#### `home`

The root URL of the application.

This view simply redirects to the main feed view (`index`) to keep routing logic separate from feed logic.

---

#### `index`

The main homepage feed.

This view combines **posts and resources into a single chronological feed**.

Features implemented include:

- subject filtering

- tag filtering

- keyword search

- content type filtering (posts or resources)

- combined sorting by creation date

- pagination

- like status detection for logged-in users

- AJAX support for partial feed updates

---

### Post Views

#### `post_detail`

Displays a single post along with:

- comments

- attached resources

Comments and resources are ordered by **like count and creation date** to highlight the most useful contributions.

Users can also submit new comments and attach resources through this view.

#### `create_post`

Allows teachers to create new posts.

Access is restricted using:

- `login_required`

- role checking for `"teacher"`

The form saves the post and assigns the logged-in user as the author.

#### `edit_post`

Allows the author of a post to edit it.

Authorization ensures that only the original author can modify the post.

#### `delete_post`

Allows the author to delete their post after confirmation.

---

## Comment Views

#### `edit_comment`

Allows a user to edit a comment they previously created.

---

#### `delete_comment`

Allows a user to delete their own comment.

---

## Resource Views

#### `edit_resource`

Allows users to edit resources they have contributed.

---

#### `delete_resource`

Allows users to delete their own resources.

---

#### `verify_resource`

Allows teachers to mark a resource as **verified**.

This acts as a quality indicator for helpful learning materials.

---

### Profile Views

#### `profile_view`

Displays a user profile page including:

- profile information

- posts created by the user

- resources shared by the user

Posts and resources are combined into a chronological feed similar to the homepage.

Filtering options remain available for subject, tags, and search.

---

#### `edit_profile`

Allows a logged-in user to update their profile information.

---

### Authentication Views

#### `register_view`

Handles user registration.

When a user registers:

- a new `User` is created

- their chosen role is stored in the associated `Profile`

- the user is automatically logged in

---

#### `login_view`

Handles user authentication using Django's built-in authentication form.

---

#### `logout_view`

Logs out the current user and redirects them to the homepage.

---

## Voting Views

#### `like_post`

Allows users to like or unlike a post.

Users cannot like their own posts.

AJAX responses allow the frontend to update like counts dynamically.

---

#### `like_comment`

Allows users to like or unlike comments.

---

#### `like_resource`

Allows users to like or unlike shared resources.

---

## Subject Views

#### `subject_list_view`

Displays all subjects along with counts of:

- posts

- resources

This helps users navigate learning topics.

---

#### `subject_detail_view`

Displays content associated with a specific subject.

Users can filter results by:

- tag

- search query

- content type

Posts and resources are merged into a combined feed similar to the homepage.

---

### Utility Views

#### `get_subject_tags`

An AJAX endpoint used to dynamically retrieve tags associated with a selected subject.

This allows the interface to update filtering options without refreshing the page.

## URL Structure

The URL configuration maps incoming requests to the appropriate views.

Routes are grouped by feature area.

---

### Home

| URL | Description       |
| --- | ----------------- |
| `/` | Main content feed |

---

### Posts

| URL                    | Description       |
| ---------------------- | ----------------- |
| `/create/`             | Create a new post |
| `/post/<slug>/`        | View post         |
| `/post/<slug>/edit/`   | Edit post         |
| `/post/<slug>/delete/` | Delete post       |

---

### Comments

| URL                     | Description    |
| ----------------------- | -------------- |
| `/comment/<id>/edit/`   | Edit comment   |
| `/comment/<id>/delete/` | Delete comment |

---

### Resources

| URL                      | Description     |
| ------------------------ | --------------- |
| `/resource/<id>/edit/`   | Edit resource   |
| `/resource/<id>/delete/` | Delete resource |
| `/verify-resource/<id>/` | Verify resource |

---

### Voting

| URL                    | Description          |
| ---------------------- | -------------------- |
| `/like-post/<id>/`     | Like/unlike post     |
| `/like-comment/<id>/`  | Like/unlike comment  |
| `/like-resource/<id>/` | Like/unlike resource |

---

### Profiles

| URL                    | Description  |
| ---------------------- | ------------ |
| `/profile/<username>/` | View profile |
| `/profile/edit/`       | Edit profile |

---

### Subjects

| URL                 | Description    |
| ------------------- | -------------- |
| `/subjects/`        | List subjects  |
| `/subjects/<slug>/` | Subject detail |

---

### Authentication

| URL          | Description       |
| ------------ | ----------------- |
| `/register/` | User registration |
| `/login/`    | Login             |
| `/logout/`   | Logout            |

---

### AJAX

| URL                  | Description                         |
| -------------------- | ----------------------------------- |
| `/get-subject-tags/` | Returns tags for a selected subject |

## Technologies Used

Django

- Main web framework for backend, ORM, authentication, and routing.

SQLite

- Default database for development and testing.

HTML/CSS/JavaScript

- Frontend structure, styling, and interactivity.

jQuery

- Simplifies AJAX requests and DOM manipulation.

Summernote

- Rich text editor for post content creation.

Bootstrap (or custom CSS)

- Responsive layout and UI components.

Heroku

- Deployment platform for hosting the app.

Python

- Core programming language for backend logic.

Django Messaging Framework

- Provides user feedback (success/error messages).

Django Forms

- Handles user input and validation.

Django Authentication

- Manages user registration, login, logout, and permissions.

AJAX

- Enables dynamic UI updates (likes, filtering, search, etc.).

Django Admin

- Used for admin-level management and teacher role assignment.

Git

- Version control for codebase management.

Environment Variables

- Securely manage secrets and configuration.

### HTML and CSS

## Testing Procedures

- Manual and automated testing steps
- Bugs found and fixes applied
- Screenshots or test logs

## Deployment Instructions

- Step-by-step guide for deploying (Heroku or other)
- Environment variables, .gitignore, secrets management
- Link to live site (if available)

## Security Features

- Passwords/secrets protected via environment variables
- DEBUG mode off in production
- User permissions and authentication

## Development Process

- Git workflow: frequent, descriptive commits
- Branch strategy (if used)
- Summary of development stages

## Attribution

- Credit for external code, libraries, tutorials

## Screenshots & Demo

- Screenshots of UI and features
- Link to demo video (optional)

## Known Issues & Future Improvements

- List any known bugs or limitations
- Suggestions for enhancements

---
