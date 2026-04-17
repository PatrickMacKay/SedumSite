#!/usr/bin/env python3
import re

# Read the original file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new About section
new_about = '''    <section id = "about"class="section about">
        <div class="about-intro">
            <h2>About Us</h2>

            <p>
                Hello, we're Jad and Patty! We came to Nova Scotia for university in 2018, 
                and fell in love with this beautiful province. We have a long history of building, 
                from systems to saloons. We feel that the cross section of our expertise in engineering 
                and management, as well as our extensive joint experience in restorative forestry, 
                allows us to bring a fresh perspective to inspiring and innovative projects. 
            </p>
        </div>

        <div class="about-person">
            <div>
                <p>
                    <strong>Patrick (he/him)</strong> holds a bachelor's degree in electrical engineering, 
                    with a focus on robotics and power distribution. He has spent several years developing 
                    a wide knowledge base for designing and building just about anything. He can often be 
                    found biking around town, or surfing at (REDACTED).
                </p>
            </div>
            <img src="sedum_images/patty_pic.JPEG" alt="Patrick">
        </div>

        <div class="about-person">
            <img src="sedum_images/jad_pic.JPG" alt="Jad">
            <div>
                <p>
                    <strong>Jad (he/him)</strong> holds a bachelor's degree in entrepreneurial management, 
                    and has spent several years honing his skills in the roles of operations management and 
                    event coordination. He is a true handyman, and can be located if you follow the sound of 
                    puttering and handtools. 
                </p>
            </div>
        </div>

        <div class="about-intro">
            <p>
                Both are often found spinning wildly on local dance floors.
            </p>
        </div>
    </section>'''

# Find and replace the About section using regex
pattern = r'    <!-- ABOUT -->.*?    </section>\n\n<section id = "services"'
replacement = f'''    <!-- ABOUT -->
{new_about}

<section id = "services"'''

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Add the banner section before closing div tags
banner_section = '''
<section class="section" style="padding: 40px; text-align: center;">
    <img src="sedum_images/jadnpatty_banner.JPG" alt="Jad and Patty Banner" style="width: 100%; max-width: 800px; border-radius: 6px;">
</section>
'''

# Insert before the closing divs
content = content.replace('</div>\n</div>\n\n</body>', f'{banner_section}\n</div>\n</div>\n\n</body>')

# Write the modified content back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ HTML file updated successfully!")
print("  - Restructured About section with individual images for Jad and Patrick")
print("  - Added banner section at the bottom")
