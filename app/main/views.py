from flask import render_template, request, redirect, url_for,abort,flash
from flask_login import login_required,current_user
from . import main
from .forms import PitchForm,UpdateProfileForm,CommentForm
from ..import db
from ..models import User, Pitch, Comment,Upvote,Downvote


@main.route('/')
def index():
    title = "Welcome to Pitches Platform!"
    return render_template('index.html', title=title)


@main.route('/user/<uname>&<id_user>')
@login_required
def profile(uname, id_user):
    user = User.query.filter_by(username = uname).first()

    title = f"{uname.capitalize()}'s Profile"

    get_pitches = Pitch.query.filter_by(user_id = id_user).all()
    get_comments = Comment.query.filter_by(user_id = id_user).all()
    get_upvotes = Upvote.query.filter_by(user_id= id_user).all()
    get_downvotes = Downvote.query.filter_by(id_user = id_user).all()
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user, title=title, pitches_no = get_pitches, comments_no = get_comments, likes_no = get_upvotes, dislikes_no = get_downvotes)

@main.route('/home/like/<int:id>', methods = ['GET','POST'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    like_pitch = Upvote(user = current_user, pitching_id=id)
    like_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))

@main.route('/home/dislike/<int:id>', methods = ['GET','POST'])
@login_required
def dislike(id):
    get_pitches = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    dislike_pitch = Upvote(user = current_user, pitching_id=id)
    dislike_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))



@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Home | One Minute Pitch'    
    return render_template('home.html', title = title, pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):
    
    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()
    

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment | One Minute Pitch'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)








    