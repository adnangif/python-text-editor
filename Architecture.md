## Project Title: Text Editor

  
  

**Decision:** Use Repository Architecture for Text Editor Development

  

**Reasoning:**
By organizing the text editor's functionality into distinct Components, we ensure modularity, scalability, and maintainability. Each component focuses on specific tasks, making it easier to understand, develop, and maintain the text editor codebase. Additionally, the optional components (Language Support and Extensions/Plugins) provide flexibility for extending the editor's functionality based on specific requirements or user preferences.

**Repository Architecture Components for Text Editor**

1.  **Open**
2.  **Save**
3.  **Save As**
4.  **Auto Save**
5.  **Copy**
6.  **Paste**
7.  **Undo/Redo**
8.  **Highlight**
9.  **Find All**
10.  **Replace All**
11.  **Copy All**


<br>
<br>
  
 ![alt text](<sdp project Architecture.png>)

<p style="text-align: center;">Figure: Diagram of Layered Repository Pattern</p>