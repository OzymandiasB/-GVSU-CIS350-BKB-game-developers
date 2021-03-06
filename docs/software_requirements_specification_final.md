# Overview
We wanted to add our own original twist on top of a classic timeless game Tetris. The goal is to add more shapes,a personal choice of different music specific powerups, and more. We want the game to feel like a modern spin that would be produced from a company that already rehashes out old classics perhaps like nintendo recreating mario.

# Software Requirements
The section will first list three categories of functional requirements, then list three categories of non-functional requirements, each with a minimum of five requirements.
  
## Functional Requirements
### Pieces
| 1.0 | Requirement |
| :-------------: | :----------: |
| FR 1.1 | The user shall be able to rotate the piece that is falling. |
| FR 1.2 | The user shall be able to move the piece left and right horizontally. |
| FR 1.3 | The user shall be able to lock a piece into place by placing it on top of another piece, or by placing it on the lowest point of the bounds available.|
| FR 1.4 | The user shall be able to push and rotate the piece at the bounds of the board, without the piece going over bounds. |
| FR 1.5 | The user shall be able to clear the blocks out by filling a row completely. |
  
### Menu Navigations
| 2.0 | Requirement |
| :-------------: | :----------: |
| FR 2.1 | The user shall be able to navigate the menu screen to access different game options and documentation. |
| FR 2.2 | The user shall be able to actively change the difficulty while the game is still running by navigating to the options and back to the game. |
| FR 2.3 | The software shall allow users to set a legacy mode from the menu if they wish to play the original Tetris without all the add-ons. |
| FR 2.4 | The user shall be able to restart the game from the main menu. |
| FR 2.5 | The software shall display instructions on how to restart the game when the game is over.|

### Media
| 3.0 | Requirement |
| :-------------: | :----------: |
| FR 3.1 | The user shall be allowed to manually set the song in the beginning of the program.        |
| FR 3.2 | The software shall change the music when the user clears a row. |
| FR 3.3 | The software shall change the background image when the user clears a row. |
| FR 3.4 | Navigating to different screens shall change the background images. |
| FR 3.5 | The software shall change songs after the current song ends. |

## Non-Functional Requirements
### Menu Navigations
| 1.0 | Requirement |
| :-------------: | :----------: |
| NFR1.1 | The menu shall have documentation describing game functionality, new block designs, and how to function the game.|
| NFR1.2 | The menu screen background shall not be changed until the user navigates to another page. |
| NFR1.3 | The software shall change screens instantaneously when navigating the different menu screens.  |
| NFR1.4 | The software’s menu shall change difficulties within one second. |
| NFR1.5 | The user shall be able to access any menu screen of the game from another screen within 2 inputs (click or press escape). |


### Media
| 2.0 | Requirement |
| :-------------: | :----------: |
| NFR2.1 | The software shall have different background images for each menu screen.|
| NFR2.2 | There shall be no buffer or lag in between song changes.|
| NFR2.3 | The software shall contain a library of five different songs.  |
| NFR2.4 | The software shall contain a library of five different background images. |
| NFR2.5 | All song files shall be MPEG-1 Audio Layer III (MP3) format. |
| NFR2.6 | All the song files shall be Joint Photographic Experts Group (jpeg) format. |


### Design
| 3.0 | Requirement |
| :-------------: | :----------: |
| NFR3.1 | Software shall use a font that is easily readable to the user.|
| NFR3.2 | Software shall use a red and blue color scheme for buttons that will not interfere with the background image. |
| NFR3.3 | Software shall use white and turquoise colored font that will not interfere with the background image.  |
| NFR3.4 | Software shall use a window format of (1024, 1000). |
| NFR3.5 | Buttons shall be placed in a manner that allows maximal viewing of background. |

# Software Artifacts
This section works to show different diagrams and lists we made during the development of the project.
* [Gantt.pdf](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/docs/GANT.pdf)
* [Proposal](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/docs/proposal-template.md) 
* [Task list](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/docs/List_Tasks.pdf)
* [Menu description](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/artifacts/use_case_diagrams/menu_description)
* [Case diagram for game](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/artifacts/use_case_diagrams/use_case_diagram_level.pdf)
* [Case diagram for manual](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/artifacts/use_case_diagrams/use_case_diagram_manual.pdf)
* [Case diagram menu](https://github.com/OzymandiasB/-GVSU-CIS350-BKB-game-developers/blob/master/artifacts/use_case_diagrams/use_case_diagram_menu.pdf)

