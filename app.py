import streamlit as st
# from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Derek Westjohn, Data Analyst
##### *Resume* 
''')

# image = Image.open('photo.jpg')
# st.image(image, width=125)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Passionate Analyst with an emphasis on data-processing and data-wrangling, as well as building visualization insight and machine-learning applications.
- Strong verbal and written communication skills as demonstrated by extensive technical trainings and presentations as a department leader.
- Strong organizational management as an acting business consultant liason for a large clientele pool.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/dwest85/project_showcase" target="_blank">Project Showcase</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#latest-education">Latest Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#latest-work-experience">Latest Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Latest Education
''')

txt('**Data Science Certification Bootcamp** (Data Analytics|Science), *Michigan State University*',
'2021-2022')
st.markdown('''
- Completion grade: `96.29% (A)`
- Capstone supervised machine-learning project titled: `Covid-19 Death Prediction Application based on Socio-Economic Data Analysis (found in Project Showcase)` 
- Completed project-showcase featuring: `VBA, Python, Matplotlib, SQL|SQLite, HTML|CSS, JavaScript|APIs|Scraping, Plotly, Tableau, R, Sci-kit Learn|TensorFlow|Spark|Hadoop`
''')
st.write(" ")

txt('**Bachelors of Science** (Computer Science), *Oregon State University*',
'2022-Current')
st.markdown('''
- Focus: `Data|Cyber Security emphasis`
- Application: `To strengthen my established data analytical skills and programming abilities.`
''')
st.write(" ")

#####################
st.markdown('''
## Latest Work Experience
''')

txt('**Data Analyst|Lead Technology Specialist**, Subway Development, Michigan and Ohio',
'2017-Current')
st.markdown('''
- Developing analytical insight through the process of data wrangling|cleansing in order to provide grouped visualization and direction for company goals.
- Working directly with the ownership|head management team to brainstorm and produce new technologies to streamline daily tasks and responsibilites. 
- Assist our clients directly with IT-based assistance when troubleshooting field-related issues.
- Provide technical training presentations for our clientele on several business portals|platforms.
- Maintain|Manage the office training website to provide useful training content for our clientele.
- Provide installation|troubleshooting to company Point-of-Sale systems and software for our clientele. 
''')
st.write(" ")

txt('**R&D|Operational Team Member**, SPI Pharma Inc., Grand Haven, Michigan',
'2008-2016')
st.markdown('''
- Worked closely with the R&D team while creating pilot trials to be used for future validations|patents.
- Heavy focus on following SOPs and working with different testing methods to ensure the products met proper guidelines.
- Daily team-based projects and collaborations to achieve company goals.
''')
st.write(" ")

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Java`, `Julia`, `R`, `Linux`, `Git`, `PowerShell`, `Batch`')
txt3('Data processing|wrangling', '`SQL`, `SQLite`, `MongoDB`, `POSTGRESQL`, `pandas`, `numpy`, `Beautiful Soup`, `selenium`')
txt3('Data visualization', '`Tableau`, `PowerBI`, `matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development Programming', '`Javascript`, `HTML`, `CSS`, `Flask`, `plotly dash`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`')
st.write(" ")

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/derek-westjohn-82154662')
txt2('Facebook', 'https://www.facebook.com/derek.westjohn')
