# Guitar-Learning-Blog

![device view](/static/images/readmeimages/guitairblog-devices.png)

## Table of Contents

- Project Rationale & Purpose
- Target Audience
- Design & Wireframes
  - Main Page Wireframes
    - Navbar
    - Home Feed Page (index.html)
    - Profile Page (profile.html)
    - Subject Page (subject.html)
    - Subject Detail Page (subject_detail.html)
    - Post Detail Page (post_detail.html)
- Features Overview
  - CRUD for profile, posts, comments and resources
  - Authentication & user profiles
  - Likes/voting system
  - Resource verification by teachers
  - Filtering, search, sort & pagination
  - AJAX updates for dynamic UX
  - Responsive design
- UX & Accessibility
  - First Time Visitor
  - Registered Student (Role: Beginner - Advanced)
  - Teacher User
  - Returning User
- Data Schema & Configuration
  - Data Entity Relationship Table
- Relationship Overview
  - User Relationships
  - Content Structure
  - Voting System
  - Summary
- Architechture Overview
  - Application Architecture
- Models
  - Tag
  - Post
  - Comment
  - Resource
  - Like
- Forms
  - Register Forms
  - PostForm
  - CommentForm
  - ResourceForm
  - ProfileForm
- Views
  - Feed Views
    - home
    - index
  - Post Views
    - post_detail
    - create_post
    - edit_post
    - delete_post
  - Comment Views
    - edit_comment
    - delete_comment
  - Resource Views
    - edit_resource
    - delete_resource
    - verify_resource
  - Profile Views
    - profile_view
    - edit_profile
  - Authentication Views
    - register_view
    - login_view
    - logout_view
  - Voting Views
    - like_post
    - like_comment
    - like_resource
  - Subject Views
    - subject_list_view
    - subject_detail_view
  - Utility Views
    - get_subject_tags
- URL Structure
  - Home
  - Posts
  - Comments
  - Resources
  - Voting
  - Profiles
  - Subjects
  - Authentication
  - AJAX
- Technologies Used
  - HTML and CSS
- Testing Procedures
  - User Story Testing
    - User Story 1: As a Beginner Level User– Discovering beginner content
    - User Story 2: As a Beginner Level User– Getting help in discussions
    - User Story 3. As a Beginner - Advanced User – Using recommended resources
- Deployment Instructions
- Security Features
- Development Process
  - User Story Testing
    - User Story 1: As a Beginner Level User– Discovering beginner content
    - User Story 2: As a Beginner Level User– Getting help in discussions
    - User Story 3. As a Beginner - Advanced User – Using recommended resources
    - User Story 4. Intermediate - Advanced User – Filtering by technique
    - User Story 5. Intermediate - Advanced User– Sharing resources
    - User Story 6. Teacher Users– Curating content
    - User Story 7. All Users - Visually readable content
  - Manual testing overview
  - Lighthouse Testing Reports
    - Index
    - Profile
    - Profile Edit
    - Subjects
    - Create Post
  - HTML, CSS and JS Validation
  - Bugs & Fixes
    - Issue 1: Subject and Tag filters not filtering/ breaking filtering. on Profile and Index Feeds
    - Issue 2: Edit Profile as 'teacher' roles available to change but teacher role not available.

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

## Design & Wireframes

### Design Choices

As this is a blog, best practises dictate to ensure clear readibility as the priority with well structured information. Looking at sites like www.reddit.com, a light, high contrast color approach would fit best for this project. With heavy use of bootstrap for simple device scalability and layout.

#### Font

Montserrat and Varela round chosen as clear and well rounded language. The sans-serif font family is well recommended for people with reading disabilities due to it's clearly spaced lettering. Ideal for a blog.

h1, h2, h3, h4, h5
font-family: "montserrat", sans-serif;
font-weight: 600;
letter-spacing: 0.5px;

.navbar-brand
font-family: "varela Round", sans-serif;
font-size: 1.4rem;

#### Color

Primary use of white and black for cards and the following color for main background, as the site is guitar based I chose a color similar to the typical wood that you would get on an acoustic guitar.

background-color: #f5e0c4

### Main Page Wireframes

The following are basic layout wireframes for the main navigatable pages on the site. The edit and create functions will use a summernote widget with basic window functionality for simplicity.

#### Navbar

A simple bootstrap navbar with logo on left and links to the profile, create post (teacher role only function), home feed and login/out.

![navbar wireframe](/static/images/readmeimages/readme-guitairblog-wireframe-navbar.png)

#### Home Feed Page (index.html)

The landing page for the site, will provide a basic overview of the site via the header cards and subject information and links, with a quick access to the home feed below which will show the latest posts and resources with filter functionality.
![index wireframe](/static/images/readmeimages/readme-guitairblog-wireframe-index.png)

#### Profile Page (profile.html)

A users' personal profile page including the heading of their name a long with a short, optional bio field that the user can edit for themselves, some stats also showing their upvoting stats. Below this, a personal feed showing the user's contribution (filtered by user).
![profile wireframe](/static/images/readmeimages/readme-guitairblog-wireframe-profile.png)

#### Subject Page (subject.html)

The main navigation by subject page, a short heading and description. This will be automatically pulled from the django DB and editable in the admin panel.
The subjects will display via card format with a short description, with CTA buttons to direct the user to the subject detail page for more specific reading.
![subject wireframe](/static/images/readmeimages/readme-guitairblog-wireframe-subject.png)

#### Subject Detail Page (subject_detail.html)

The subject details purpose is to display the content of the subject via long description and provide underneat, a subject specific feed that allows the user to see related resources and posts which have been categorised under this specific subject.
![subject detail](/static/images/readmeimages/readme-guitairblog-wireframe-subject-detail.png)

#### Post Detail Page (post_detail.html)

A page create by teacher or above permission roles to allow users to comment with optional shared resource.
This feed is the only one which shows comments and comments with nested resource.

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
   ![first time 1 detail](/static/images/readmeimages/readme-guitairblog-ux-firsttimevisitor-1.png)

3. Selects a subject.

![first time 2 detail](/static/images/readmeimages/readme-guitairblog-ux-firsttimevisitor-2.png) 4. Views posts by subject. 5. Opens a post.
![first time 3 detail](/static/images/readmeimages/readme-guitairblog-ux-firsttimevisitor-3.png) 6. Reads comments and shared resources. 7. Registers to participate in community.
![first time 4 detail](/static/images/readmeimages/readme-guitairblog-ux-firsttimevisitor-4.png)

Value:

1. Clear subject organisation and orientation.
2. Ranked comments with upvote system and teacher verification.
3. Quick onboarding via register form.

### Registered Student (Role: Beginner - Advanced)

Journey:

1. Logs into account
2. Reads recent posts via homefeed

![revisit 1 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-1.png)

3. Navigates or filters to subject for posts and resources.

![revisit 2 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-2.png)

4. leaves comment and optionally shares resources for posts.

![revisit 3 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-3.png)
![revisit 4 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-4.png)

5. votes on helpful resources.

![revisit 5 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-5.png)

6. See's own profile for their contribution.

![revisit 6 detail](/static/images/readmeimages/readme-guitairblog-ux-revisitvisitor-6.png)

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

![teacher 1 detail](/static/images/readmeimages/readme-guitairblog-ux-teacher-1.png)

5. Engages with students comments and resources.
6. Moderates and monitors resources shared under their posts.

![teacher 2 detail](/static/images/readmeimages/readme-guitairblog-ux-teacher-2.png)

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

HTML Layouts:

- Your main layout is defined in [base.html], which uses Bootstrap 5 via CDN for responsive design and layout.
- Content is wrapped in a `.container` with `mt-4` for margin, and blocks are used for Django template inheritance.
- Other templates (login, register, profile, post, subject, etc.) extend this base and use Bootstrap grid classes like `.row`, `.col-md-6`, `.col-lg-5`, `.justify-content-center`, and `.align-items-center` for layout and alignment.
- Forms and cards are styled with Bootstrap classes (`.card`, `.shadow-sm`, `.p-4`, `.btn`, `.btn-primary`, `.w-100`).

Bootstrap Usage:

- Bootstrap 5 is included for layout, grid, and component styling.
- Classes like `.container`, `.row`, `.col-*`, `.btn`, `.card`, `.shadow-sm`, `.mb-4`, `.mt-3`, `.w-100`, `.justify-content-center`, `.align-items-center` are used throughout templates.
- Bootstrap's JS bundle is loaded for interactive components.

CSS:

- Custom theme styles are in [style.css] and similar files in staticfiles.
- Global styles set background color, font families (`opensans`, `montserrat`, `varela Round`), and text color.
- Navbar styles: `.navbar`, `.navbar-brand`, `.nav-link` for color, font-weight, and hover effects.
- Page headers, subject headers, and cards have custom backgrounds, padding, border-radius, and border.
- Tag badges: `.tag-badge` for inline display, background, color, border-radius, font-size, and hover transitions.
- Responsive adjustments for mobile and tablet layouts are handled in admin and custom CSS files.
- Admin and CKEditor styles are included for dashboard, forms, widgets, and rich text editing.

Other Notable Features:

- jQuery is included for custom scripting.
- Summernote and CKEditor are used for rich text editing, with their own CSS.
- Custom classes for submit button alignment, tag containers, and form text.

Summary:

- The project uses Bootstrap for layout and responsiveness, with custom CSS for theme and component styling.
- HTML templates are structured for modularity and reuse, leveraging Django's template inheritance.
- Rich text editing and admin interfaces are styled with additional CSS.

## Testing Procedures

### User Story Testing

#### User Story 1: As a Beginner Level User– Discovering beginner content

Acceptance Criteria

1. User selects “Beginner” during onboarding or in profile
   Passed - See image
   ![user story 1a](/static/images/readmeimages/readme-guitairblog-userstories-1-a.png)

2. User can see level labels on every post
   Passed - See image
   ![user story 1b](/static/images/readmeimages/readme-guitairblog-userstories-1-b.png)

3. User can override filters manually if desired
   Passed - See image
   ![user story 1c](/static/images/readmeimages/readme-guitairblog-userstories-1-c.png)

#### User Story 2: As a Beginner Level User– Getting help in discussions

Acceptance Criteria

1. User can post a reply or question on a learning post
   Passed - See image
   ![user story 2a](/static/images/readmeimages/readme-guitairblog-userstories-2-a.png)

2. Replies display author
   Passed - See image
   ![user story 2b](/static/images/readmeimages/readme-guitairblog-userstories-2-b.png)

3. Teacher approvals are visually distinct
   Passed - See image
   ![user story 2c](/static/images/readmeimages/readme-guitairblog-userstories-2-c.png)

4. Replies can be upvoted
   Passed - See image
   ![user story 2c](/static/images/readmeimages/readme-guitairblog-userstories-2-d.png)

#### User Story 3. As a Beginner - Advanced User – Using recommended resources

Acceptance Criteria

1. Learning posts display a “Resources” section
2. Resources include title, type, and description
3. User can upvote resources

Passed - See image
![user story 3a](/static/images/readmeimages/readme-guitairblog-userstories-3-a.png)

#### User Story 4. Intermediate - Advanced User – Filtering by technique

Acceptance Criteria

1. Posts support multiple tags (e.g. speed, rhythm)
2. User can filter by subject and tag
   Passed - See image
   ![user story 4a](/static/images/readmeimages/readme-guitairblog-userstories-4-a.png)

#### User Story 5. Intermediate - Advanced User– Sharing resources

Acceptance Criteria

1. User can add a resource via URL
2. User must select resource type
3. User must provide a short justification

Passed - See image
![user story 5a](/static/images/readmeimages/readme-guitairblog-userstories-5-a.png)

#### User Story 6. Teacher Users– Curating content

Acceptance Criteria

1. Teachers have a “Verify Advice” action
2. Verified replies show a badge
3. Only teachers can verify content
4. Verification is reversible (moderation)

Passed - See image
![user story 2c](/static/images/readmeimages/readme-guitairblog-userstories-2-c.png)

#### User Story 7. All Users - Visually readable content

1. High accessibility
   Passed - Using lighthouse testing to ensure score over 80 for accessibility.

2. High contrast between background and font
   Passed - Use of white/light tan background with black/brown font.

3. Digestable layouts with intuitive design
   Passed - Use of cards and simple format to ensure.

4. Device Accessible
   Passed - Use of bootstrap for content stacking, lighthouse testing on both desktop and mobile to ensure.

### Manual testing overview

Primarily done via Google Chrome.

I tested the python queries as I implemented them through production with periodic testing on the deployed site to ensure no major bugs.
Once this was satisfactory, I tested all actions and navigation by at least 1 account in every role. Below is the table I used to guide this process and record any issues to be fixed.

![user testing](/static/images/readmeimages/readme-guitairblog-manual-test-sheet.png)

### Lighthouse Testing Reports

I used the lighthouse extension to test overall performance, accessibility, best practises and SEO scoring on each html template. My goal was to acheive over 80 in all where posssible, here are the page's peeformance reports:

#### Index

![lighthouse index desktop](/static/images/readmeimages/readme-guitairblog-index-lighthouse-desktop.png)
![lighthouse index mobile](/static/images/readmeimages/readme-guitairblog-index-lighthouse-mobile.png)

#### Profile

![lighthouse profile desktop](/static/images/readmeimages/readme-guitairblog-profile-lighthouse-desktop.png)
![lighthouse profile mobile](/static/images/readmeimages/readme-guitairblog-profile-lighthouse-mobile.png)

#### Profile Edit

![lighthouse profile edit desktop](/static/images/readmeimages/readme-guitairblog-profile-edit-lighthouse-desktop.png)
![lighthouse profile edit mobile](/static/images/readmeimages/readme-guitairblog-profile-edit-lighthouse-mobile.png)

#### Subjects

![lighthouse subjects desktop](/static/images/readmeimages/readme-guitairblog-subjects-lighthouse-desktop.png)
![lighthouse subjects mobile](/static/images/readmeimages/readme-guitairblog-subjects-lighthouse-mobile.png)

#### Create Post

![lighthouse create desktop](/static/images/readmeimages/readme-guitairblog-createpost-lighthouse-desktop.png)
![lighthouse create mobile](/static/images/readmeimages/readme-guitairblog-createpost-lighthouse-mobile.png)

### HTML, CSS and JS Validation

#### HTML Validation

All pages passed html validation with the exception of the following errors which appear on all text edit pages and are due to the 'Summernote' widget.
The widget is required for free rich text capability on this website. As the errors pertain to this and appearing within the script, and also summernote has little to no documentation. This is an unavoidable error due to requiring the widget to scale correctly for the device via forcing dimensions, so I have passed this for deployment/ live. The following are the errors which appear.

Error: Bad value true for attribute hidden on element textarea.

From line 193, column 21; to line 193, column 95

textarea name"content" cols"40" rows"10" id"id_content" hidden"true">↩</tex

Error: Element style not allowed as child of element div in this context. (Suppressing further errors from this subtree.)

From line 197, column 1; to line 197, column 7

</script>↩<style>↩ifram

Contexts in which element style may be used:
Where metadata content is expected.
In a noscript element that is a child of a head element.
Content model for element div:
If the element is a child of a dl element: One or more dt elements followed by one or more dd elements, optionally intermixed with script-supporting elements.
Otherwise, if the element is a descendant of an option element: Zero or more option element inner content elements.
Otherwise, if the element is a descendant of an optgroup element: Zero or more optgroup element inner content elements.
Otherwise, if the element is a descendant of a select element: Zero or more select element inner content elements.
Otherwise: flow content.
Error: Attribute cols not allowed on element div at this point.

From line 207, column 1; to line 207, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute rows not allowed on element div at this point.

From line 207, column 1; to line 207, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute width not allowed on element div at this point.

From line 207, column 1; to line 207, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute height not allowed on element div at this point.

From line 207, column 1; to line 207, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.

From line 208, column 3; to line 208, column 112

#ERROR!

Warning: The frameborder attribute on the iframe element is obsolete. Use CSS instead.

From line 208, column 3; to line 208, column 112

#ERROR!

Error: Bad value true for attribute hidden on element textarea.

From line 225, column 21; to line 225, column 121

textarea name"resource_description" cols"40" rows"10" id"id_resource_description" hidden"true">↩</tex

Error: Element style not allowed as child of element div in this context. (Suppressing further errors from this subtree.)

From line 229, column 1; to line 229, column 7

/script>↩<style>↩ifram

Contexts in which element style may be used:
Where metadata content is expected.
In a noscript element that is a child of a head element.
Content model for element div:
If the element is a child of a dl element: One or more dt elements followed by one or more dd elements, optionally intermixed with script-supporting elements.
Otherwise, if the element is a descendant of an option element: Zero or more option element inner content elements.
Otherwise, if the element is a descendant of an optgroup element: Zero or more optgroup element inner content elements.
Otherwise, if the element is a descendant of a select element: Zero or more select element inner content elements.
Otherwise: flow content.
Error: Attribute cols not allowed on element div at this point.

From line 239, column 1; to line 239, column 75

/style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute rows not allowed on element div at this point.

From line 239, column 1; to line 239, column 75

/style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute width not allowed on element div at this point.

From line 239, column 1; to line 239, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Attribute height not allowed on element div at this point.

From line 239, column 1; to line 239, column 75

↩</style>↩<div class"summernote-div" cols"40" rows"10" width"100%" height"300">↩ <if

Attributes for element div:
Global attributes
Error: Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.

From line 240, column 3; to line 240, column 138

#ERROR!

Warning: The frameborder attribute on the iframe element is obsolete. Use CSS instead.

From line 240, column 3; to line 240, column 138

"300">↩ <iframe id"id_resource_description_iframe" src"/summernote/editor/id_resource_description/" frameborder"0" width"100%" height"300"></ifra

#### CSS Validation (style.css W3)

![css validation](/static/images/readmeimages/readme-guitairblog-css-validation.png)

#### Javascript (script.js JSHINT)

![jshint validation](/static/images/readmeimages/readme-guitarblog-jshint-validation.png)

### Bugs & Fixes

The following are the main bugs and fixes applied during the testing phase of my project:

#### Issue 1: Subject and Tag filters not filtering/ breaking filtering. on Profile and Index Feeds

Expected result: When selecting a subject via filter drop down, the tags assigned to the subject should appear and be clickable.

Troubleshooting:

Step 1: As I had recently mass-deleted posts via admin panel, my first step was to clean the database for orphan tags in case this was causing any issues with the database. I used the commands and removed 90 orphaned tags:

![issue 1](/static/images/readmeimages/readme-guitairblog-issues-1.png)

Step 1 Outcome: Fail

Fail: However did succeed in cleaning data base as screenshot shows 'Tag Orphans' did require purging following some deletions of content via Django Admin

Step 2
I had discovered through further investigation that the url for subject filter was not returning the slug but the pk value.
Solution Steps

1. Dropdown Value and Data Attribute
   Changed the subject dropdown <option> value to use the subject’s slug (for filtering in the view).
   Added/ensured a data-pk attribute on each <option> (for AJAX/tag filtering).
   Set the "All Subjects" option to:
2. JavaScript Update
   Updated the tag filtering AJAX to use the subject’s primary key from data-pk:
   Ensured the AJAX does not run if "All Subjects" is selected:
3. Template Consistency
   Applied these changes to both profile.html and index.html to ensure consistent behavior across your site.
4. No Model or Migration Changes Needed
5. Result
   Subject filtering now works using slugs (clean URLs).
   Tag filtering by subject works via AJAX, using the subject’s primary key.

Result: No more broken dropdowns or missing tags.

Commit Message: "user test: feed filter tags not returning correct content"

#### Issue 2: Edit Profile as 'teacher' roles available to change but teacher role not available.

Expected result: Only applicable levels to show.

Fix:

Removed the dropdown field entirely for teacher role, as the teacher is moderator and highest level role beneath admin, there is no need for this user to downgrade to student and/or is already engaged with the site admin.

in edit_profile.html
![issue 2](/static/images/readmeimages/readme-guitairblog-issues-2.png)

## Deployment Instructions

### Local Development

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd MSP3-Guitar-Blog
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the app:**
   Open your browser at [http://localhost:8000](http://localhost:8000)

---

### Deploying to Heroku

1. **Install the Heroku CLI** (if not already installed):  
   [Heroku CLI Download](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login to Heroku:**

   ```sh
   heroku login
   ```

3. **Create a new Heroku app:**

   ```sh
   heroku create your-app-name
   ```

4. **Set up environment variables:**  
   Set `SECRET_KEY`, `DEBUG=False`, and any other required variables:

   ```sh
   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set DEBUG=False
   ```

5. **Add Heroku Postgres (if using a database):**

   ```sh
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Push code to Heroku:**

   ```sh
   git push heroku main
   # or, if using master branch:
   git push heroku master
   ```

7. **Run migrations on Heroku:**

   ```sh
   heroku run python manage.py migrate
   ```

8. **Create a superuser on Heroku (optional):**

   ```sh
   heroku run python manage.py createsuperuser
   ```

9. **Open your app:**
   ```sh
   heroku open
   ```

---

**Notes:**

- Ensure your `requirements.txt`, `Procfile`, and `runtime.txt` are up to date.
- Collect static files if needed:
  ```sh
  python manage.py collectstatic
  ```
- Use environment variables for all secrets and sensitive settings. Never commit secrets to version control.
- Add `*.pyc`, `.env`, `.venv/`, `db.sqlite3`, and other sensitive files to `.gitignore`.

## Security Features

This project follows Django security best practices. All sensitive information, such as secret keys and database credentials, is managed using environment variables and never committed to version control. The application enforces `DEBUG = False` in production to prevent exposure of sensitive error details. User authentication and permissions are handled through Django’s built-in system, ensuring that only authorized users can access or modify protected resources. Additional security measures include password hashing, CSRF protection, and regular updates to dependencies.

## Development Process

All development for this project was performed on the main branch using Git for version control. Changes were committed frequently with descriptive messages to document progress and key decisions. The workflow was linear, with each new feature or bugfix added directly to the main branch. The project progressed through several stages: initial planning and requirements gathering, database and model design, implementation of core features, user interface development, thorough manual testing, and deployment. This approach ensured a clear and traceable development history suitable for a solo developer.

## Attribution

- Credit for external code, libraries, tutorials

---
