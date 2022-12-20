from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Xiaochen", "Zheng"]
    email = "xzheng.ethz@gmail.com"
    twitter = "XiaochenZheng3"
    github = "xcvil"
    linkedin = "xiaochen-zheng-a058429b"
    bio_text = f"""
                <p>I am a first-year PhD student on machine learning and data science in <a href="https://www.ics.uzh.ch/en/">Institute for Computational Science</a> at University of Zürich, and an associated PhD student at <a href="https://ai.ethz.ch"> ETH AI Center</a>.</p>
                <!-- <p>
                    <span style="font-weight: bold;">Research:</span>
                    I am excited about complex problems that can be tackled with learning-based systems. Currently, my research focuses on 3D vision, and I am interested in how machines can infer 3D representations from sparse observations. Further, I am big fan of neural scene representations, \ie, how scenes are best represented in learning-based systems using deep neural networks. 
                </p> -->
                <p>
                    <span style="font-weight: bold;">Bio:</span> 
                    I obtained my master degree from ETH Zürich in 2021, and my bachelor degree from Dalian University of Technology in 2017.
                    <!-- During my Bachelor studies, I spent one year at the <a href="https://www.ub.edu/web/portal/en/" target="_blank">University of Barcelona</a>, Spain, funded by the ERASMUS program. -->
                    <!-- Following my interest in computer science, I then moved to Scotland to gain my Master's degree in Advanced Computer Science at the  -->
                    <!-- In October 2018, I started my PhD in computer vision / machine learning in the <a href="https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/home/" target="_blank">AVG group</a> at the <a href ="https://is.mpg.de/" target="_blank">Max Planck Institute for Intelligent Systems</a> in Tübingen, Germany, under the supervision of <a href="http://cvlibs.net/" target="_blank">Andreas Geiger</a>.  -->
                    <!-- In 2021 I joined <a href="https://research.google/teams/brain/">Google Brain</a> for an internship and subsequently as a student researcher. -->
                </p>
                <p>For any inquiries, feel free to reach out to me via mail!</p>
                <p>
                    <a href="mailto:xzheng.ethz@gmail.com" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/XiaochenZheng3" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=KUeQNfwAAAAJ&hl=en&authuser=1" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Google Scholar</a>
                    <a href="https://github.com/xcvil" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/xiaochen-zheng-a058429b" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This website is based on the lightweight and easy-to-use template from Michael Niemeyer. <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Check out his github repository for instructions on how to use it!</a>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Devis Tuia': 'https://people.epfl.ch/devis.tuia',
        'Benjamin Kellenberger': 'https://bkellenb.github.io',
        'Rui Gong': 'https://scholar.google.com/citations?user=4St8MdYAAAAJ&hl=en',
        'Irena Hajnsek': 'https://scholar.google.de/citations?user=UDDXUBcAAAAJ&hl=de',
        'Laurence Yang': 'https://scholar.google.ca/citations?user=a39Yz5cAAAAJ&hl=en',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Xiaochen Zheng', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        if 'html' in entry.fields.keys():
            s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""
        else:
            s += f"""<a href="{entry.fields['pdf']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <img src="assets/img/profile.png" class="img-thumbnail" width="280px" alt="Profile picture">
            </div>
        </div>
        <div class="row" style="margin-top: 1em;">
            <div class="col-sm-12" style="">
                <h4>Publications</h4>
                {pub}
            </div>
        </div>
        <!-- <div class="row" style="margin-top: 3em;"> -->
            <!-- <div class="col-sm-12" style=""> -->
                <!-- <h4>Talks</h4> -->
                <!-- {talks} -->
            <!-- </div> -->
        <!-- </div> -->
        <div class="row" style="margin-top: 1em;">
            <div class="col-sm-12" style="">
                <h4>Supervision</h4>
                <p>Xingyu Chen (2022 - 2023), master student at ETH Zurich.</p>
                <p>Richard Affolter (2022 - 2023), master student at ETH Zurich.</p>
            </div>
        </div>
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')