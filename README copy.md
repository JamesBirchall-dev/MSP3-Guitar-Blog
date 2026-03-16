# Guitar-Learning-Blog

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

## UX & Accessibility

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
- Description of models and relationships
- Where database/configuration settings are managed (e.g., settings.py)

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
