import argparse
import sys
from generator import PasswordGenerator

def main():
    parser = argparse.ArgumentParser(
        description="Generate secure passwords from a seed string",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py -s "myseed" -l 20
  python cli.py --seed "myseed" --length 20
  python cli.py -s "myseed"  # Uses default length of 15
        """
    )
    
    parser.add_argument(
        '-s', '--seed',
        type=str,
        required=True,
        help='Seed string to generate password'
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=15,
        help='Password length (default: 15, range: 4-72)'
    )
    
    parser.add_argument(
        '-c', '--check',
        action='store_true',
        help='Show password strength check result'
    )
    
    args = parser.parse_args()
    
    # Validate length
    if args.length < 4 or args.length > 72:
        print("Error: Length must be between 4 and 72", file=sys.stderr)
        sys.exit(1)
    
    # Generate password
    pwd_gen = PasswordGenerator(length=args.length, seed_seq=args.seed)
    pwd_gen.generate_password()
    
    # Output
    print(pwd_gen.pw)
    
    if args.check:
        strength = "✓ Strong" if pwd_gen.check else "✗ Weak"
        print(f"Strength: {strength}", file=sys.stderr)

if __name__ == '__main__':
    main()
