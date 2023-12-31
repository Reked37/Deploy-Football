"""making tables

Revision ID: d53bd666eff7
Revises: 
Create Date: 2023-11-21 09:08:47.233969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53bd666eff7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('mascot', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coaches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('coaching_position', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_coaches_team_id_teams')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('home_team_id', sa.Integer(), nullable=False),
    sa.Column('away_team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['away_team_id'], ['teams.id'], name=op.f('fk_matches_away_team_id_teams')),
    sa.ForeignKeyConstraint(['home_team_id'], ['teams.id'], name=op.f('fk_matches_home_team_id_teams')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('jersey_number', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_players_team_id_teams')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_coach_association',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('coach_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['coach_id'], ['coaches.id'], name=op.f('fk_player_coach_association_coach_id_coaches')),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], name=op.f('fk_player_coach_association_player_id_players'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_coach_association')
    op.drop_table('players')
    op.drop_table('matches')
    op.drop_table('coaches')
    op.drop_table('teams')
    # ### end Alembic commands ###
