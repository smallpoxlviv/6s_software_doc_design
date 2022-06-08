import re
import sys
from string import Template

section_templates = {'WeekModel': Template('$i,name$i,description$i,["video_url$i"],["reading_url$i"],["quizz_url$i"]\n')}


def generate_csv(filename):
    with open(filename, 'w+') as file:
        for section, template in section_templates.items():
            file.write(section + '\n')
            for i in range(1, 250):
                file.write(template.substitute(i=i))
            file.write('\n')


def write_from_csv_to_db(filename, sections):
    with open(filename, 'r+') as file:
        for part in re.split(r'\n\n+', file.read()):
            rows = part.split('\n')
            for row in rows:
                for section_name in sections:
                    if section_name == row.strip():
                        cls = getattr(sys.modules['software_doc_design.models'], section_name)
                        for row in rows[1:]:
                            args = row.split(',')
                            obj = cls(data_list=args)
                            # if section_name == 'Story':
                            #     user = User.get_by_pk(randint(1, len(rows) - 1))
                            #     user.stories.append(obj)
                            #     user.save()
                            # else:
                            obj.save()
