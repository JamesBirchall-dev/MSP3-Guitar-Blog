# MSP3-Guitar-Blog

## Scope & Content

### Scope

Concept: The site is a reddit-style guitar learning forum for all levels users to see, share and rate learning content. The website will be split into clear subjects and feeds and with relevant tags for filtering and with a teacher-level moderator user for verifying content posted providing a clear teacher vs learner dynamic.
The posts themselves will be rateable with a verification badge that can be applied by the teachers/ moderators. The posts will be able to share external resources such as youtube videos, guitar tabs and articles.

### Content & Wireframes

#### 1. Global Structure - global navbar

Primaary Navigation (top)

![Navigation-Wireframe](https://github.com/JamesBirchall-dev/imagehost/blob/main/learn-guitar-forum-wireframes-navigation.png?raw=true)

- Home/ Logo - Directing to home page
- Feed - Personalised forum/ blog feed
- Subjects - Dropdown menu displaying each blog section: Practise Drills, Songs, Equipment, Theory, Tips, Listening
- User Level badges - Filter learning levels (Beginner, Intermediate, Advanced, Teacher)
- Search bar - Posts and tags
- Profile - user's saved profile, posts and logout functionality

#### 2. Home Page/ Main Feed Page - index.html

![Feed-Page-Wireframe](https://github.com/JamesBirchall-dev/imagehost/blob/main/learn-guitar-forum-wireframes-homepage.png?raw=true)

Filter Bar:

- Fiter: Tags, User level badge
- Sort: Most helpful (upvote count)

Posts in order of visual heirarchy:

- Upvote count for the post
- Title - Learning post page
- User Level Badge - range view for multiple selection
- Count of replies on the post
- Count of resources

#### 3. Subject Landing Pagee

Designed for navigation via posts for users by clicking on the subject links. Gets the user to think about the subject by clearly displaying the title, meaning and subtopics for the subject.

![Subject-Landing-Wireframe](https://github.com/JamesBirchall-dev/imagehost/blob/main/learn-guitar-forum-wireframes-subject-landing-page.png?raw=true)

- Header and Sub Header for basic description of the subject.
- Feed with collapsed posts with subtopic filters availabe.

#### 4. Post Page - posts/

- post_detail.html
- post_create.html
- post_edit.html

This is the post page which main purpose is to display the post in the most visually spaced and 'clutterless' way possible providing maximum readibility and user engagement.

- Post Header - very visually dominant header and sub header
- Content Card - maximum visual reading for users to provide clear tips to other users
- Resources Card - similar to content card visually with use of icons and vote counts for user navigation. Badges for teacher levels to add extra value. Ability to add a resource as a user. Also filterable by user level.
- Add Learning Resource - Contains resource type (youtube, article or tab), url for the resource and a brief explanation of it's usefulness.
- Discussion Card - For user replies, use of stacked with spacing as per standard forum formnat.

#### 5. User Profile Page

The main purpose of this page is to display the user's profile and contribution to the network.
User fields Card:

- Username - unique name chosen at registration
- User Level - chosen at registration - beginner, intermediate, advanced or teacher
- Reputation - count of upvotes on posts
- Instruments - chosen at registration

Contribution Card:

- Post history sorted by upvote (high to low) then by date.

#### 6. Registration Page

Basic onboarding page for the user to register onto the site. The data is then used to personalise the user's profile, feeds and posts.

- Username with validation
- Guitar level - choose - beginner, intermediate, advanced or teacher
- Instruments - Electric, Acoustic or Bass

## UX

### User Stories

#### User Story 1. Beginner Level User– Discovering beginner content

Acceptance Criteria

- User selects “Beginner” during onboarding or in profile
- Feed defaults to showing Beginner-level posts
- User can see level labels on every post
- User can override filters manually if desired

#### User Story 2. Beginner Level User– Getting help in discussions

Acceptance Criteria

- User can post a reply or question on a learning post
- Replies display author level badge
- Teacher replies are visually distinct
- Replies can be upvoted

#### User Story 3. Beginner – Using recommended resources

Acceptance Criteria

- Learning posts display a “Resources” section
- Resources include title, type, and description
- User can upvote resources
- Resources are sorted by usefulness score by default

#### User Story 4. Intermediate User – Filtering by technique

Acceptance Criteria

- Posts support multiple tags (e.g. speed, rhythm)
- User can filter by subject and tag
- Filters update results without page reload (UX)
- Filter state is clearly visible

#### User Story 5. Intermediate User– Sharing resources

Acceptance Criteria

- User can add a resource via URL
- User must select resource type
- User must provide a short justification
- Resource appears immediately in the post

#### User Story 6. Advanced Users – Weighted advice

Acceptance Criteria

- User level affects vote weight internally
- UI does NOT expose raw calculations to users
- Replies are sorted by usefulness score
- Higher-quality replies naturally surface

#### User Story 7. Advanced Users– Curating content

Acceptance Criteria

- Advanced users can upvote/downvote resources
- Vote affects resource ranking
- Resource ranking updates dynamically
- Low-rated resources are visually deemphasized

#### User Story 8. Teacher/ Moderator User – Verifying guidance

Acceptance Criteria

- Teachers have a “Verify Advice” action
- Verified replies show a badge
- Only teachers can verify content
- Verification is reversible (moderation)

#### User Story 9. Teacher/ Moderator User Level – Identifying unanswered

Acceptance Criteria

- System detects posts with unanswered questions
- Teachers have a filtered view or indicator
- Sorting by “Needs help” is available
- Clicking opens discussion directly

## User Profile

## User Journey

## Interaction Design

## Accessbility & Best Practises

## Visual Design

## Data Model Design

1. User

- writes multiple posts, replies and resources
- one profile

2. Post

- belongs to one subject only
- can have many replies
- can have many resources
- can have many tags

3. Reply

- belongs to one post
- can be verified by a teacher

4. Resource

- belongs to one post

5. Votes

- applies to posts, replies and resources

6. Verification

- applies to posts
